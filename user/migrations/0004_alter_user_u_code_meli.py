# Generated by Django 4.2.6 on 2023-10-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_u_code_meli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_code_meli',
            field=models.CharField(db_index=True, max_length=10, unique=True, verbose_name='code meli'),
        ),
    ]
