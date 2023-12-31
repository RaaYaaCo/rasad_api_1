from django.utils.translation import gettext as _
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import UserSerializer, UserCodeSerializer, WholesalerStoreSerializer, WholesalerStoreCodeSerializer, \
                         OtherSerializer, OtherCodeSerializer, LoginSerializer, LoginSerializerCreateAccessToken, \
                         LogoutSerializer, ForgetPasswordSerializer, ForgetPasswordCodeSerializer, NewPasswordSerializer

from .models import User
from .utils import code, get_tokens
from rasad_api.settings import REDIS_OTP_CODE, REDIS_OTP_CODE_TIME, REDIS_JWT_TOKEN, REDIS_REFRESH_TIME


class UserGenericAPIView(GenericAPIView):
    """
        This view is for saving the information of the user in the session.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.session.get('register', {})
        request.session['register'] = serializer.data
        request.session.modified = True
        otp_code = code(length=5)
        REDIS_OTP_CODE.set(name=serializer.validated_data['u_phone_number'],
                           value=otp_code,
                           ex=REDIS_OTP_CODE_TIME)
        data1 = {
            'first_name': request.session['register']['first_name'],
            'last_name': request.session['register']['last_name'],
            'code_melli': request.session['register']['u_code_meli'],
            'phone_number': request.session['register']['u_phone_number'],
        }
        data2 = {
            'otp_code': otp_code,
               }

        return Response(data={"Information": data1, "otp_code": data2, 'msg': 'Data is stored in the session'},
                        status=status.HTTP_201_CREATED)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class UserCodeGenericAPIView(GenericAPIView):
    """
        This view is for saving the information of the user in the database.
    """
    serializer_class = UserCodeSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        register = request.session.get('register')  # Value of session's key.
        try:
            otp_code = REDIS_OTP_CODE.get(register['u_phone_number'])
            otp_code = otp_code.decode('utf-8')
            if otp_code == serializer.validated_data['otp_code']:
                register['is_active'] = True
                serializer = UserSerializer(data=register)
                serializer.is_valid(raise_exception=False)
                serializer.save()
                user = User.objects.get(u_phone_number=register['u_phone_number'])
                group = Group.objects.get(name='مشتری')
                group.user_set.add(user)
                group.save()
                tokens = get_tokens(user)
                access_token = tokens['Access']
                refresh_token = tokens['Refresh']
                REDIS_JWT_TOKEN.set(name=refresh_token,
                                    value=refresh_token,
                                    ex=REDIS_REFRESH_TIME)
                data1 = {
                    'first_name': request.session['register']['first_name'],
                    'last_name': request.session['register']['last_name'],
                    'code_meli': request.session['register']['u_code_meli'],
                    'phone_number': request.session['register']['u_phone_number'],
                    'group': group.name
                }
                data2 = {
                    "AccessToken": access_token,
                    "RefreshToken": REDIS_JWT_TOKEN.get(refresh_token),
                       }
                request.session['register'].clear()
                request.session.modified = True
                return Response(data={'Information': data1, 'Tokens': data2, 'msg': 'Data is stored in the database'},
                                status=status.HTTP_201_CREATED)

            return Response(data={'msg': _('The code is wrong')},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_massage = str(e)
            return Response(data={'msg': _('There is no such code in redis'), 'error': error_massage},
                            status=status.HTTP_400_BAD_REQUEST)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class WholesalerStoreGenericAPIView(GenericAPIView):
    """
        This view is for saving the information of the wholesaler and store in the session.
    """
    serializer_class = WholesalerStoreSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.session.get('register', {})
        request.session['register'] = serializer.data
        request.session.modified = True
        otp_code = code(length=5)
        REDIS_OTP_CODE.set(name=serializer.data['phone_number'],
                           value=otp_code,
                           ex=REDIS_OTP_CODE_TIME)
        request.session['register']['slug'] = request.session['register']['name'].replace(' ', '-')
        data1 = {
            'first_name': request.session['register']['first_name'],
            'last_name': request.session['register']['last_name'],
            'code_meli': request.session['register']['code_meli'],
            'phone_number': request.session['register']['phone_number'],
            'name': request.session['register']['name'],
            'description': request.session['register']['description'],
            'address': request.session['register']['address'],
            'location': request.session['register']['location'],
            'license': request.session['register']['license'],
            'postal_code': request.session['register']['postal_code'],
            'slug': request.session['register']['slug']
        }
        data2 = {
            'otp_code': otp_code,
               }
        return Response(data={'Information': data1, 'otp_code': data2, 'msg': 'Data is stored in the session'},
                        status=status.HTTP_201_CREATED)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class WholesalerStoreCodeGenericAPIView(GenericAPIView):
    """
        This view is for saving the information of the wholesaler and store  in the database.
    """
    serializer_class = WholesalerStoreCodeSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=False)
        register = request.session.get('register')  # Value of session's key.
        try:
            otp_code = REDIS_OTP_CODE.get(register['phone_number'])
            otp_code = otp_code.decode('utf-8')
            if otp_code == request.data['otp_code']:
                serializer = WholesalerStoreSerializer(data=register)
                serializer.is_valid(raise_exception=False)
                serializer.save()
                user = User.objects.get(u_phone_number=register['phone_number'])
                user.is_active = False
                user.save()
                group = Group.objects.get(name='فروشگاه')
                group.user_set.add(user)
                group.save()
                data = {
                    'first_name': request.session['register']['first_name'],
                    'last_name': request.session['register']['last_name'],
                    'code_melli': request.session['register']['code_meli'],
                    'phone_number': request.session['register']['phone_number'],
                    'name': request.session['register']['name'],
                    'description': request.session['register']['description'],
                    'address': request.session['register']['address'],
                    'location': request.session['register']['location'],
                    'license': request.session['register']['license'],
                    'postal_code': request.session['register']['postal_code'],
                    'group': group.name,
                    'slug': request.session['register']['slug']
                }
                request.session['register'].clear()
                request.session.modified = True
                return Response(data={'Information': data, 'msg': 'Data is stored in the database'},
                                status=status.HTTP_201_CREATED)

            return Response(data={'msg': _('The code is wrong')},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_massage = str(e)
            return Response(data={'msg': _('There is no such code in redis'), 'error': error_massage},
                            status=status.HTTP_400_BAD_REQUEST)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class OtherGenericAPIView(GenericAPIView):
    """
        This view is for saving the information of other in the session.
    """
    queryset = User.objects.all()
    serializer_class = OtherSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.session.get('register', {})
        request.session['register'] = serializer.data
        request.session.modified = True
        otp_code = code(length=5)
        REDIS_OTP_CODE.set(name=serializer.validated_data['u_phone_number'],
                           value=otp_code,
                           ex=REDIS_OTP_CODE_TIME)
        data1 = {
            'first_name': request.session['register']['first_name'],
            'last_name': request.session['register']['last_name'],
            'code_melli': request.session['register']['u_code_meli'],
            'phone_number': request.session['register']['u_phone_number'],
            'group': request.session['register']['group'],
        }
        data2 = {
            'otp_code': otp_code,
               }
        return Response(data={"Information": data1, "otp_code": data2, 'msg': 'the data is stored in the session'},
                        status=status.HTTP_201_CREATED)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class OtherCodeGenericAPIView(GenericAPIView):
    """
        This view is for saving the information of the other in the database.
    """
    serializer_class = OtherCodeSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        register = request.session.get('register')  # Value of session's key.
        try:
            otp_code = REDIS_OTP_CODE.get(register['u_phone_number'])
            otp_code = otp_code.decode('utf-8')
            if otp_code == serializer.validated_data['otp_code']:
                serializer = UserSerializer(data=register)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                user = User.objects.get(u_phone_number=register['u_phone_number'])
                user.is_active = False
                user.save()
                group = Group.objects.get(name=request.session['register']['group'])
                group.user_set.add(user)
                group.save()
                data = {
                    'first_name': request.session['register']['first_name'],
                    'last_name': request.session['register']['last_name'],
                    'code_melli': request.session['register']['u_code_meli'],
                    'phone_number': request.session['register']['u_phone_number'],
                    'group': request.session['register']['group'],
                }
                request.session['register'].clear()
                request.session.modified = True
                return Response(data={'Information': data, 'msg': 'the data is stored in the database'},
                                status=status.HTTP_201_CREATED)

            return Response(data={'msg': _('The code is wrong')},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_massage = str(e)
            return Response(data={'msg': _('There is no such code in redis'), 'error': error_massage},
                            status=status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class LoginGenericAPIView(GenericAPIView):
    """
        This view is for "login".
    """
    serializer_class = LoginSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        try:
            user = User.objects.get(u_phone_number=request.data['u_phone_number'])
            group = Group.objects.get(user=user)
            if user.check_password(request.data['password']) and user.is_active == True:
                tokens = get_tokens(user)
                access_token = tokens['Access']
                refresh_token = tokens['Refresh']
                REDIS_JWT_TOKEN.set(name=refresh_token, value=refresh_token, ex=REDIS_REFRESH_TIME)
                data = {
                    "user": {
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'code_meli': user.u_code_meli,
                        'phone_number': user.u_phone_number,
                        'group': group.name,
                    },
                    'token': {
                        "access": access_token,
                        "refresh": REDIS_JWT_TOKEN.get(refresh_token)
                    }
                }
                return Response(data=data, status=status.HTTP_201_CREATED)
            return Response({'msg': _('You are not allowed to enter')})
        except Exception as e:
            error_message = str(e)
            return Response(data={'msg': error_message})

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class LoginAPIViewCreateAccess(GenericAPIView):
    """
        This view is for "Creating New Access Token".
    """
    serializer_class = LoginSerializerCreateAccessToken

    def post(self, request: Request) -> Response:
        try:
            token = request.data['refresh_token']
            REDIS_JWT_TOKEN.delete(token)
            token = RefreshToken(token)
            user = User.objects.get(id=token['user_id'])
            group = Group.objects.get(user=user)
            access_refresh_token = get_tokens(user)
            access_token = access_refresh_token['Access']
            refresh_token = access_refresh_token['Refresh']
            REDIS_JWT_TOKEN.set(name=refresh_token, value=refresh_token, ex=REDIS_REFRESH_TIME)
            data = {
                "user": {
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'code_meli': user.u_code_meli,
                        'phone_number': user.u_phone_number,
                        'group': group.name
                },
                "new access": access_token,
                "new refresh": REDIS_JWT_TOKEN.get(refresh_token)
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_message = str(e)
            return Response({'message': _('Token is expired'), 'error': error_message})

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class LogoutAPIView(GenericAPIView):
    """
        This view is for "Logout".
    """
    serializer_class = LogoutSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        refresh_token = request.data['refresh_token']
        if REDIS_JWT_TOKEN.exists(refresh_token):
            REDIS_JWT_TOKEN.delete(refresh_token)
            return Response({"message": _("You are logged out successfully")})
        else:
            return Response({"message": _("There is no refresh token in redis")})

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


class ForgetPasswordAPIView(GenericAPIView):
    """
        This view is for creating the otp code for creating the new password.
    """
    serializer_class = ForgetPasswordSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        request.session.get('forget', {})
        request.session['forget'] = serializer.data
        request.session.modified = True
        otp_code = code(length=5)
        REDIS_OTP_CODE.set(name=serializer.validated_data['phone_number'],
                           value=otp_code,
                           ex=REDIS_OTP_CODE_TIME)
        data = {
            'otp_code': otp_code,
        }
        return Response(data={"otp_code": data}, status=status.HTTP_201_CREATED)


class ForgetPasswordCodeAPIView(GenericAPIView):
    """
        This view is for checking the otp code for confirming the right user.
    """
    serializer_class = ForgetPasswordCodeSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        register = request.session.get('forget')  # Value of session's key.
        try:
            otp_code = REDIS_OTP_CODE.get(register['phone_number'])
            otp_code = otp_code.decode('utf-8')
            if otp_code == serializer.validated_data['otp_code']:
                data = {
                    'phone_number': request.session['forget']['phone_number'],
                    'msg': _('The code is correct.')
                }
                return Response(data=data, status=status.HTTP_201_CREATED)

            return Response(data={'msg': _('The code is wrong')},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_massage = str(e)
            return Response(data={'msg': _('There is no such code in redis'), 'error': error_massage},
                            status=status.HTTP_400_BAD_REQUEST)


class NewPasswordSerializerAPIView(GenericAPIView):
    """
        This view is for creating new password.
    """
    serializer_class = NewPasswordSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        register = request.session.get('forget')  # Value of session's key.
        try:
            user = User.objects.get(u_phone_number=register['phone_number'])
            user.password = make_password(serializer.data['new_password_1'])
            user.save()
            request.session['forget'].clear()
            request.session.modified = True
            data = {
                'msg': _('The new password is created successfully'),
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_massage = str(e)
            return Response(data={'error': error_massage}, status=status.HTTP_400_BAD_REQUEST)
