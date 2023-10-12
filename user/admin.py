from django.contrib import admin
from .models import UserType, Store, User

# Register your models here.


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['ut_title']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_license', 's_address', 's_postal_code']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'u_phone_number', 'u_code_meli']


