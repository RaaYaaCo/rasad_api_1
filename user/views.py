from django.utils.translation import gettext as _

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, UserCodeSerializer
from .models import User
from .utils import code, get_tokens
from rasad_api.settings import REDIS_OTP_CODE, REDIS_OTP_CODE_TIME, REDIS_JWT_TOKEN, REDIS_REFRESH_TIME

# Create your views here.


class UserGenericAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        request.session.get('register', {})
        request.session['register'] = serializer.data
        request.session.modified = True
        otp_code = code(length=5)
        REDIS_OTP_CODE.set(name=serializer.validated_data['u_phone_number'], value=otp_code, ex=REDIS_OTP_CODE_TIME)
        data = {
            'otp_code': otp_code,
               }
        return Response(data={"a": serializer.data, "b": data}, status=status.HTTP_201_CREATED)


class UserCodeGenericAPIView(GenericAPIView):
    serializer_class = UserCodeSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        register = request.session.get('register')  # Value of session's key.
        try:
            otp_code = REDIS_OTP_CODE.get(register['u_phone_number'])
            otp_code = otp_code.decode('utf-8')
            if otp_code == serializer.data['otp_code']:
                register['is_active'] = True
                serializer = UserSerializer(data=register)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                # ---------------------------
                user = User.objects.get(u_phone_number=register['u_phone_number'])
                tokens = get_tokens(user)
                access_token = tokens['Access']
                refresh_token = tokens['Refresh']
                REDIS_JWT_TOKEN.set(name=refresh_token, value=refresh_token, ex=REDIS_REFRESH_TIME)
                data = {
                    "AccessToken": access_token,
                     "RefreshToken": REDIS_JWT_TOKEN.get(refresh_token),
                       }
                del request.session['register']
                request.session.modified = True
                # -------------------------------
                return Response(data={'Information': serializer.data, 'Tokens': data}, status=status.HTTP_201_CREATED)

            return Response(data={'msg': _('The code is wrong')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(data={'msg': _('There is no such code in redis')}, status=status.HTTP_400_BAD_REQUEST)
