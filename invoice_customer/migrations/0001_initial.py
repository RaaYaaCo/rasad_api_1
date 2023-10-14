# Generated by Django 4.2.6 on 2023-10-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ic_date_time', models.DateTimeField(auto_now_add=True, verbose_name='date time')),
            ],
            options={
                'verbose_name': 'Invoice Customer',
                'verbose_name_plural': 'Invoices Customer',
            },
        ),
        migrations.CreateModel(
            name='InvoiceCustomerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ici_weight', models.FloatField(verbose_name='weight')),
            ],
            options={
                'verbose_name': 'Invoice Customer Item',
            },
        ),
        migrations.CreateModel(
            name='ProductEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi_price', models.PositiveIntegerField(verbose_name='Invoice Sales price')),
                ('sale_price', models.PositiveIntegerField(verbose_name='sale price')),
                ('pe_weight', models.PositiveIntegerField(verbose_name='weight')),
                ('pe_is_active', models.BooleanField(default=True, verbose_name='active/deactivate')),
                ('pe_date_time', models.DateTimeField(auto_now_add=True, verbose_name='date time')),
                ('pe_update_time', models.DateTimeField(auto_now_add=True, verbose_name='update time')),
            ],
            options={
                'verbose_name': 'Product Entity',
                'verbose_name_plural': 'Products Entity',
            },
        ),
    ]
