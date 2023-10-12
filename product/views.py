from django.utils.translation import gettext as _

from rest_framework.generics import CreateAPIView, ListCreateAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core.utils import translate
from .serializers import ProductTypeSerializers, UnitSerializer,\
                         DegreeSerializer, ProductSerializers
from .models import ProductType, Degree, Unit, Product


class ProductTypeView(CreateAPIView):
    serializer_class = ProductTypeSerializers
    queryset = ProductType.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(Request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data={'data': serializer.data, 'msg': _('you select the product type successfully')},
                        status=status.HTTP_201_CREATED)


class ProductTypeDetailView(RetrieveUpdateAPIView):
    serializer_class = ProductTypeSerializers
    queryset = ProductType.objects.all()

    def retrieve(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class DegreeView(CreateAPIView):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(Request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data={'data': serializer.data, 'msg': _('you add degree successfully')},
                        status=status.HTTP_201_CREATED)


class DegreeDetailView(CreateAPIView):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()

    def retrieve(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class UnitView(CreateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(Request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data={'data': serializer.data, 'msg': _('you add unit successfully')},
                        status=status.HTTP_201_CREATED)


class UnitDetailView(CreateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def retrieve(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filterset_fields = ['p_name', 'pt_id', 'd_id']

    def list(self, request: Request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.serializer_class(instance=instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request, *args, **kwargs):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'p_slug'

    def retrieve(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

