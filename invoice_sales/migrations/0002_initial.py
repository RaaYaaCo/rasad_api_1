# Generated by Django 4.2.6 on 2023-10-13 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice_sales', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicesales',
            name='u_store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='storeSales', to=settings.AUTH_USER_MODEL, verbose_name='store'),
        ),
        migrations.AddField(
            model_name='invoicesales',
            name='u_wholesaler_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wholesalerSales', to=settings.AUTH_USER_MODEL, verbose_name='wholesaler'),
        ),
    ]
