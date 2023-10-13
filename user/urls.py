from django.urls import path
from .views import UserGenericAPIView, UserCodeGenericAPIView, WholesalerStoreGenericAPIView, \
    WholesalerStoreCodeGenericAPIView, OtherGenericAPIView, OtherCodeGenericAPIView

app_name = 'user'

urlpatterns = [
    path('register/customer/', UserGenericAPIView.as_view(), name='register-customer'),
    path('register/customer/save/', UserCodeGenericAPIView.as_view(), name='register-customer-save'),
    path('register/whole-store/', WholesalerStoreGenericAPIView.as_view(), name='register-whole-store'),
    path('register/whole-store/save/', WholesalerStoreCodeGenericAPIView.as_view(), name='register-whole-store-save'),
    path('register/other/', OtherGenericAPIView.as_view(), name='register-other'),
    path('register/other/save/', OtherCodeGenericAPIView.as_view(), name='register-other-save')
]