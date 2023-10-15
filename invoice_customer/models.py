from django.db import models
from django.utils.translation import gettext as _

from invoice_sales.models import InvoiceSales
from product.models import Product, ProductPrice
from user.models import User, Store


# Create your models here.


class InvoiceCustomer(models.Model):
    u_store_id = models.ForeignKey(Store, on_delete=models.PROTECT,
                                   db_index=True,
                                   verbose_name=_('store'),
                                   related_name='storeCustomer'
                                   )
    u_customer_id = models.ForeignKey(User, on_delete=models.PROTECT,
                                      db_index=True,
                                      verbose_name=_('customer'),
                                      related_name='customerInvoiceCustomer'
                                      )
    ic_date_time = models.DateTimeField(auto_now_add=True, verbose_name=_('date time'))

    def __str__(self):
        return f'{self.u_store_id.s_name} / {self.u_customer_id.u_phone_number}'

    class Meta:
        verbose_name = _('Invoice Customer')
        verbose_name_plural = _('Invoices Customer')


class ProductEntity(models.Model):
    u_store_id = models.ForeignKey(Store, on_delete=models.PROTECT,
                                   db_index=True,
                                   verbose_name=_('store'),
                                   related_name='storeProductEntity'
                                   )
    isi_id = models.ForeignKey(InvoiceSales, on_delete=models.PROTECT, db_index=True, verbose_name=_('Invoice Sales'))
    p_id = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_('product'))
    isi_price = models.PositiveIntegerField(verbose_name=_('Invoice Sales price'))
    sale_price = models.PositiveIntegerField(verbose_name=_('sale price'))
    pe_weight = models.PositiveIntegerField(verbose_name=_('weight'))
    pe_is_active = models.BooleanField(default=True, verbose_name=_('active/deactivate'))
    pe_date_time = models.DateTimeField(auto_now_add=True, verbose_name=_('date time'))
    pe_update_time = models.DateTimeField(auto_now_add=True, verbose_name=_('update time'))

    def __str__(self):
        return f'{self.u_store_id.s_name} / {self.p_id.p_name} / {self.sale_price}'

    class Meta:
        verbose_name = _('Product Entity')
        verbose_name_plural = _('Products Entity')


class InvoiceCustomerItem(models.Model):
    ic_id = models.ForeignKey(InvoiceCustomer, on_delete=models.CASCADE, db_index=True, verbose_name=_('Invoice'))
    p_id = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_('product'))
    ici_weight = models.FloatField(verbose_name=_('weight'))
    pe_id = models.ForeignKey(ProductEntity, on_delete=models.PROTECT, verbose_name=_('Product Price'))

    def __str__(self):
        return f'{self.ic_id.u_store_id.s_name} / {self.ic_id.u_customer_id.u_phone_number} / {self.p_id.p_name}'

    class Meta:
        verbose_name = _('Invoice Customer Item')
