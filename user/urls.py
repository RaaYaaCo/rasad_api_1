from django.urls import path
from .views import UserGenericAPIView, UserCodeGenericAPIView, WholesalerStoreGenericAPIView, \
    WholesalerStoreCodeGenericAPIView, OtherGenericAPIView, OtherCodeGenericAPIView, LoginGenericAPIView, \
    LoginAPIViewCreateAccess, LogoutAPIView, ForgetPasswordAPIView, ForgetPasswordCodeAPIView, \
    NewPasswordSerializerAPIView

app_name = 'user'

urlpatterns = [
    path('register/customer/', UserGenericAPIView.as_view(), name='register-customer'),
    path('register/customer/save/', UserCodeGenericAPIView.as_view(), name='register-customer-save'),
    path('register/whole-store/', WholesalerStoreGenericAPIView.as_view(), name='register-whole-store'),
    path('register/whole-store/save/', WholesalerStoreCodeGenericAPIView.as_view(), name='register-whole-store-save'),
    path('register/other/', OtherGenericAPIView.as_view(), name='register-other'),
    path('register/other/save/', OtherCodeGenericAPIView.as_view(), name='register-other-save'),
    path('login/', LoginGenericAPIView.as_view(), name='login-user'),
    path('login/create-token/', LoginAPIViewCreateAccess.as_view(), name='login-create-token'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='forget-password'),
    path('forget-password-code/', ForgetPasswordCodeAPIView.as_view(), name='forget-password-code'),
    path('new-password/', NewPasswordSerializerAPIView.as_view(), name='new-password')
]
