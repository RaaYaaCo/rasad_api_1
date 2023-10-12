from django.db import models
from django.utils.translation import gettext as _

from user.models import User


class Rating(models.Model):
    r_title = models.CharField(max_length=200, db_index=True, verbose_name=_('title'))


    def __str__(self):
        return f'{self.r_title}'


    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')



class RatingStore(models.Model):
    u_customer_id = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True, verbose_name=_(' customer id'),related_name='customers+')
    u_store_id = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True, verbose_name=_(' store id'))
    r_id = models.ForeignKey(Rating, on_delete=models.PROTECT, db_index=True, verbose_name=_('rating id'))
    rs_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    rs_update_time = models.DateTimeField(auto_now=True, db_index=True, verbose_name=_('updated at'))


    def __str__(self):
        return f'{self.u_customer_id}//////{self.r_id}'


    class Meta:
        verbose_name = _('Stores Rating')
        verbose_name_plural = _('Stores Ratings')


class Complaint(models.Model):
    u_customer_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('customer id'), related_name='complaints_as_customer')
    u_store_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('store id'))
    c_title = models.CharField(max_length=200, db_index=True, verbose_name=_('title'))
    c_body = models.TextField(verbose_name=_('body'))
    c_id_read_by_admin = models.BooleanField(default=False, db_index=True, verbose_name=_('read by admin'))
    c_admin_id = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name=_('admin id'), related_name='complaints_as_admin')
    c_response_admin = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('admin response'))
    c_datetime = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('created at'))
    c_update_time = models.DateTimeField(auto_now=True, db_index=True, verbose_name=_('updated at'))


    def __str__(self):
        return f'{self.u_customer_id}/////{self.c_title}'


    class Meta:
        verbose_name = _('Complaint')
        verbose_name_plural = _('Complaints')
