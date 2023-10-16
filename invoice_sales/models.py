from django.db import models
from django.utils.translation import gettext as _

from product.models import Product, ProductPrice
from user.models import User, Store


# Create your models here.


class InvoiceSales(models.Model):
    u_wholesaler_id = models.ForeignKey(User, on_delete=models.PROTECT,
                                        db_index=True,
                                        verbose_name=_('wholesaler'),
                                        related_name='wholesalerSales'
                                        )
    u_store_id = models.ForeignKey(Store, on_delete=models.PROTECT,
                                   db_index=True,
                                   verbose_name=_('store'),
                                   related_name='storeSales'
                                   )
    is_date_time = models.DateTimeField(auto_now_add=True, verbose_name=_('date time'))

    def __str__(self):
        return f'{self.u_store_id.s_name} / {self.u_wholesaler_id.u_phone_number}'

    class Meta:
        verbose_name = _('Invoice Sales')
        verbose_name_plural = _('Invoices Sales')


class InvoiceSalesItem(models.Model):
    is_id = models.ForeignKey(InvoiceSales, on_delete=models.CASCADE, db_index=True, verbose_name=_('Invoice'))
    p_id = models.ForeignKey(Product, on_delete=models.PROTECT, db_index=True, verbose_name=_('product'))
    isi_weight = models.FloatField(verbose_name=_('weight'))
    pp_id = models.ForeignKey(ProductPrice, on_delete=models.CASCADE, verbose_name=_('product price'))

    def __str__(self):
        return f'{self.is_id.u_store_id.s_name} / {self.p_id.p_name}'

    class Meta:
        verbose_name = _('Invoice Sales Item')
