from django.urls import path
from .views import UserGenericAPIView, UserCodeGenericAPIView

app_name = 'user'

urlpatterns = [
    path('register/customer/', UserGenericAPIView.as_view()),
    path('register/customer/save/', UserCodeGenericAPIView.as_view()),
]