# Generated by Django 4.2.6 on 2023-10-13 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Degree',
                'verbose_name_plural': 'Degrees',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(db_index=True, max_length=100, verbose_name='name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/images/', verbose_name='image')),
                ('p_slug', models.CharField(blank=True, db_index=True, max_length=100, unique=True, verbose_name='slug')),
                ('d_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.degree', verbose_name='degree')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Product Type',
                'verbose_name_plural': 'Products Type',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('un_title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp_price', models.PositiveIntegerField(db_index=True, verbose_name='price')),
                ('pp_is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('pp_date_time', models.DateTimeField(auto_now_add=True, verbose_name='date and time')),
                ('pp_update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product price',
                'verbose_name_plural': 'Products price',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='pt_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.producttype', verbose_name='product type'),
        ),
        migrations.AddField(
            model_name='product',
            name='un_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.unit', verbose_name='Unit'),
        ),
    ]
