from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from .models import User
from .utils import code
from rasad_api.settings import REDIS_OTP_CODE, REDIS_OTP_CODE_TIME

# Create your views here.


class UserGenericAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.session.get('register', {})
        request.session['register'] = serializer.data
        request.session.modified = True
        print(request.session.get('register'))
        otp_code = code(length=5)
        print(otp_code)
        REDIS_OTP_CODE.set(name=serializer.validated_data['u_phone_number'], value=otp_code, ex=REDIS_OTP_CODE_TIME)
        data = {
            'otp_code': otp_code,
        }
        return Response(data={"a": serializer.data, "b": data}, status=status.HTTP_201_CREATED)