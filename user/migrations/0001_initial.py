# Generated by Django 4.2.6 on 2023-10-13 13:18

from django.conf import settings
import django.contrib.auth.validators
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models
import user.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('u_phone_number', models.CharField(db_index=True, max_length=11, unique=True, validators=[user.validators.check_phone], verbose_name='phone number')),
                ('u_code_meli', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='code meli')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', user.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ut_title', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'User Type',
                'verbose_name_plural': 'User Types',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200, unique=True, verbose_name='Store Name')),
                ('s_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('s_address', models.TextField(verbose_name='Address')),
                ('s_location', django.contrib.gis.db.models.fields.GeometryField(blank=True, geography=True, null=True, srid=4326, verbose_name='Location')),
                ('s_postal_code', models.CharField(max_length=200, validators=[user.validators.isnumeric], verbose_name='Postal Code')),
                ('s_license', models.CharField(max_length=10, unique=True, validators=[user.validators.isnumeric], verbose_name='Job License')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User Id')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='ut_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.usertype', verbose_name='user type id'),
        ),
    ]
