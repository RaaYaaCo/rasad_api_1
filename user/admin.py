from django.contrib import admin
from .models import UserType, UserProfile, User

# Register your models here.


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['ut_title']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['up_address', 'up_post_code']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'u_phone_number', 'u_code_meli']


