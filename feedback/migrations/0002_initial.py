# Generated by Django 4.2.6 on 2023-10-14 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feedback', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingstore',
            name='u_customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customers+', to=settings.AUTH_USER_MODEL, verbose_name=' customer id'),
        ),
        migrations.AddField(
            model_name='ratingstore',
            name='u_store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name=' store id'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='c_admin_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='complaints_as_admin', to=settings.AUTH_USER_MODEL, verbose_name='admin id'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='u_customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='complaints_as_customer', to=settings.AUTH_USER_MODEL, verbose_name='customer id'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='u_store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='store id'),
        ),
    ]
