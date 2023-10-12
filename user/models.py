import warnings

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.deprecation import RemovedInDjango51Warning
from django.utils.translation import gettext as _
from django.contrib.gis.db import models as model

from .validators import check_phone

# Create your models here.


class UserType(models.Model):
    ut_title = models.CharField(max_length=200, db_index=True, unique=True, verbose_name=_("title"))

    def __str__(self):
        return f"{self.ut_title}"

    class Meta:
        verbose_name = _("User Type")
        verbose_name_plural = _("User Types")


class UserProfile(models.Model):
    up_address = model.TextField(verbose_name=_('address'))
    up_post_code = models.CharField(max_length=200, verbose_name=_("post code"))
    up_location = model.GeometryField(geography=True, null=True, blank=True, verbose_name=_('location'))

    def __str__(self):
        return f"{self.up_address}"

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")


class MyUserManager(BaseUserManager):
    """
        Creating a new user manager for our customized django user.
    """

    def make_random_password(
        self,
        length=10,
        allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789",
    ):
        """
        Generate a random password with the given length and given
        allowed_chars. The default value of allowed_chars does not have "I" or
        "O" or letters and digits that look similar -- just to avoid confusion.
        """
        warnings.warn(
            "BaseUserManager.make_random_password() is deprecated.",
            category=RemovedInDjango51Warning,
            stacklevel=2,
        )
        return get_random_string(length, allowed_chars)

    def create_superuser(self, username='admin', email=None, password=None, **extra_fields):
        # username = extra_fields['email']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username='admin', email=None, password=None, **extra_fields):
        # username = extra_fields['email']
        password_validation.password_changed(password)
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'u_phone_number'
    u_phone_number = models.CharField(max_length=200, db_index=True, unique=True, validators=[check_phone],
                                      verbose_name=_('phone number'))
    u_code_meli = models.CharField(max_length=10, db_index=True, unique=True, verbose_name=_("code meli"))
    ut_id = models.ForeignKey(UserType, on_delete=models.PROTECT, blank=True, null=True, verbose_name=_("user type id"))
    up_id = models.OneToOneField(UserProfile, on_delete=models.PROTECT, blank=True, null=True,
                                 verbose_name=_("user profile id"))
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.u_phone_number} / {self.u_code_meli}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
