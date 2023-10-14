from django.contrib.auth.models import AbstractUser, UserManager, Group
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.gis.db import models as model

from .validators import check_phone, isnumeric

# Create your models here.


# -------------------------------------------------------------------------------------------------


class UserType(models.Model):
    ut_title = models.CharField(max_length=200, db_index=True, unique=True, verbose_name=_("title"))

    def __str__(self):
        return f"{self.ut_title}"

    class Meta:
        verbose_name = _("User Type")
        verbose_name_plural = _("User Types")


class MyUserManager(UserManager):
    """
        Creating a new user manager for our customized django user.
    """

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('first_name', 'ali')
        username = extra_fields['u_phone_number']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('first_name', 'ali')
        username = extra_fields['u_phone_number']
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'u_phone_number'
    u_phone_number = models.CharField(max_length=11, db_index=True, unique=True, validators=[check_phone],
                                      verbose_name=_('phone number'))
    u_code_meli = models.CharField(max_length=10, db_index=True, unique=True, verbose_name=_("code meli"))
    ut_id = models.ForeignKey(UserType, on_delete=models.PROTECT, blank=True, null=True, verbose_name=_("user type id"))
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        self.username = self.u_phone_number
        # self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.u_phone_number} / {self.u_code_meli}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Store(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True, verbose_name=_("User Id"))
    s_name = models.CharField(max_length=200, unique=True, verbose_name=_("Store Name"))
    s_description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    s_address = model.TextField(verbose_name=_('Address'))
    s_location = model.GeometryField(geography=True, null=True, blank=True, verbose_name=_('Location'))
    s_postal_code = models.CharField(max_length=200, validators=[isnumeric], verbose_name=_("Postal Code"))
    s_license = models.CharField(max_length=10, unique=True, validators=[isnumeric], verbose_name=_("Job License"))
    s_slug = models.CharField(max_length=200, unique=True, verbose_name=_('slug'), blank=True)

    def __str__(self):
        return f"{self.s_name}"

    def save(self, *args, **kwargs):
        self.s_slug = self.s_name.replace(' ', '-')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")
