# Generated by Django 4.2.6 on 2023-10-13 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ie_driver', models.CharField(db_index=True, max_length=100, verbose_name='driver')),
                ('ie_full_weight', models.FloatField(verbose_name='full weight')),
                ('ie_empty_weight', models.FloatField(verbose_name='empty weight')),
                ('ie_total_weight', models.FloatField(verbose_name='total weight')),
                ('ie_date_time', models.DateTimeField(auto_now_add=True, verbose_name='date time')),
            ],
            options={
                'verbose_name': 'Invoice Entry',
                'verbose_name_plural': 'Invoices Entry',
            },
        ),
        migrations.CreateModel(
            name='InvoiceEntryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iei_weight', models.FloatField(verbose_name='weight')),
                ('ie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice_entry.invoiceentry', verbose_name='Invoice')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Invoice Entry Item',
            },
        ),
    ]
