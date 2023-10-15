from django.db import models
from django.utils.translation import gettext as _

from product.models import Product
from user.models import User


# Create your models here.


class InvoiceEntry(models.Model):
    u_wholesaler_id = models.ForeignKey(User, on_delete=models.PROTECT,
                                        db_index=True,
                                        verbose_name=_('wholesaler'),
                                        related_name='wholesalerEntry'
                                        )
    ie_driver = models.CharField(max_length=100, db_index=True, verbose_name=_('driver'))
    ie_full_weight = models.FloatField(verbose_name=_('full weight'))
    ie_empty_weight = models.FloatField(verbose_name=_('empty weight'))
    ie_total_weight = models.FloatField(verbose_name=_('total weight'))
    ie_date_time = models.DateTimeField(auto_now_add=True, verbose_name=_('date time'))

    def __str__(self):
        return f'{self.u_wholesaler_id.u_phone_number} / {self.u_wholesaler_id.first_name} {self.u_wholesaler_id.last_name}'

    class Meta:
        verbose_name = _('Invoice Entry')
        verbose_name_plural = _('Invoices Entry')


class InvoiceEntryItem(models.Model):
    ie_id = models.ForeignKey(InvoiceEntry, on_delete=models.CASCADE, db_index=True, verbose_name=_('Invoice'))
    p_id = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_('product'))
    iei_weight = models.FloatField(verbose_name=_('weight'))

    def __str__(self):
        return f'{self.ie_id.u_wholesaler_id.u_phone_number} / {self.p_id.p_name}'

    class Meta:
        verbose_name = _('Invoice Entry Item')

