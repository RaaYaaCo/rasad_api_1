from django.core.management.base import BaseCommand

from user.models import UserType
from django.contrib.auth.models import Group
from product.models import ProductType, Degree, Unit
from feedback.models import Rating


class Command(BaseCommand):

    def handle(self, *args, **options):
        # user type ------------------------------------------
        UserType.objects.get_or_create(ut_title='حقیقی')
        UserType.objects.get_or_create(ut_title='حقوقی')

        # Group ---------------------------------------------
        Group.objects.get_or_create(name='مشتری')
        Group.objects.get_or_create(name='فروشگاه')
        Group.objects.get_or_create(name='عمده فروش')
        Group.objects.get_or_create(name='بازرسان اصناف')
        Group.objects.get_or_create(name='شورای نرخ گذاری')
        Group.objects.get_or_create(name='جهاد کشاورزی')
        Group.objects.get_or_create(name='استانداری')
        Group.objects.get_or_create(name='اتاق بازرگانی')
        Group.objects.get_or_create(name='تعزیرات حکومتی')
        Group.objects.get_or_create(name='مدیران')

        # Product type -------------------------------------
        ProductType.objects.get_or_create(pt_title='میوه')
        ProductType.objects.get_or_create(pt_title='گوشت قرمز')
        ProductType.objects.get_or_create(pt_title='مرغ')
        ProductType.objects.get_or_create(pt_title='ماهی')

        # Degree --------------------------------------------
        Degree.objects.get_or_create(d_title='ممتاز')
        Degree.objects.get_or_create(d_title='درجه یک')
        Degree.objects.get_or_create(d_title='درجه دو')
        Degree.objects.get_or_create(d_title='درجه سه')
        Degree.objects.get_or_create(d_title='درجه چهار')

        # Unit ----------------------------------------------
        Unit.objects.get_or_create(un_title='کیلوگرم')
        Unit.objects.get_or_create(un_title='تن')

        # Rating --------------------------------------------
        Rating.objects.get_or_create(r_title='1')
        Rating.objects.get_or_create(r_title='2')
        Rating.objects.get_or_create(r_title='3')
        Rating.objects.get_or_create(r_title='4')
        Rating.objects.get_or_create(r_title='5')
