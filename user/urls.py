from django.urls import path
from .views import UserGenericAPIView

app_name = 'user'

urlpatterns = [
    path("register/customer/", UserGenericAPIView.as_view(), name="customer-register")
]
