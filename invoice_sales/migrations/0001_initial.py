# Generated by Django 4.2.6 on 2023-10-11 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_date_time', models.DateTimeField(auto_now_add=True, verbose_name='date time')),
            ],
            options={
                'verbose_name': 'Invoice Sales',
                'verbose_name_plural': 'Invoices Sales',
            },
        ),
        migrations.CreateModel(
            name='InvoiceSalesItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi_weight', models.FloatField(verbose_name='weight')),
                ('is_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice_sales.invoicesales', verbose_name='Invoice')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='product')),
                ('pp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productprice', verbose_name='product price')),
            ],
            options={
                'verbose_name': 'Invoice Sales Item',
            },
        ),
    ]