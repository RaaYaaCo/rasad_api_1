from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.gis.db import models as model


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


class User(AbstractUser):
    u_phone_number = models.CharField(max_length=200, db_index=True, unique=True, verbose_name=_("phone number"))
    u_code_meli = models.CharField(max_length=200, db_index=True, unique=True, verbose_name=_("code meli"))
    ut_id = models.ForeignKey(UserType, on_delete=models.CASCADE, verbose_name=_("user type id"))
    up_id = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_("user profile id"))

    def __str__(self):
        return f"{self.u_phone_number} / {self.u_code_meli}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
