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
        instance = self.queryset.all()
        serializer = self.serializer_class(instance=instance, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class StoreSearchView(generics.GenericAPIView):
    serializer_class = StoreSearchSerializer
    queryset = Store.objects.filter

    def post(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.queryset(s_name__contains=request.data['search'])
        serializer = StoreSerializer(instance, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class StoreDetailView(generics.RetrieveAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    lookup_field = 's_slug'

    def retrieve(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

