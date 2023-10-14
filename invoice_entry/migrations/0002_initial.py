# Generated by Django 4.2.6 on 2023-10-14 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice_entry', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceentry',
            name='u_wholesaler_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wholesalerEntry', to=settings.AUTH_USER_MODEL, verbose_name='wholesaler'),
        ),
    ]
