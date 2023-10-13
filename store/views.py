from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core.utils import translate
from .serializers import StoreSerializer, StoreSearchSerializer
from user.models import Store


class StoreView(generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def list(self, request: Request, *args, **kwargs):
        translate(request)
        super().list(request, *args, **kwargs)

