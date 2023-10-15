from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _

from rest_framework.generics import CreateAPIView, ListCreateAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core.utils import translate
from .serializers import ProductTypeSerializers, UnitSerializer, \
    DegreeSerializer, ProductSerializers, ProductPriceSerializer
from .models import ProductType, Degree, Unit, Product, ProductPrice


class ProductTypeView(CreateAPIView):
    serializer_class = ProductTypeSerializers
    queryset = ProductType.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(Request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
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
        serializer.save()
        return Response(data={'data': serializer.data, 'msg': _('you add degree successfully')},
                        status=status.HTTP_201_CREATED)


class DegreeDetailView(RetrieveUpdateAPIView):
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
        serializer.save()
        return Response(data={'data': serializer.data, 'msg': _('you add unit successfully')},
                        status=status.HTTP_201_CREATED)


class UnitDetailView(RetrieveUpdateAPIView):
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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({'msg': _('you can not register a product with the same name and degree')})


class ProductDetailView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "p_slug"

    def retrieve(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({'msg': _('you can not register a product with the same name and degree')})


class ProductPriceView(GenericAPIView):
    serializer_class = ProductPriceSerializer
    queryset = ProductPrice.objects.all()

    def get(self, request: Request):
        translate(request)
        instance = self.get_queryset()
        serializer = self.serializer_class(instance=instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                pervious_product_price = ProductPrice.objects.get(p_id=request.data['p_id'],
                                                                  pp_is_active=True)
                pervious_product_price.pp_is_active = False
                pervious_product_price.save()
                serializer.save()
                return Response(data={'data': serializer.data, 'msg': _('new price registered')},
                                status=status.HTTP_201_CREATED)

            except ObjectDoesNotExist:
                serializer.save()
                return Response(data={'data': serializer.data, 'msg': _('new price registered')},
                                status=status.HTTP_201_CREATED)


class EachProductPriceView(generics.GenericAPIView):
    serializer_class = ProductPriceSerializer
    queryset = ProductPrice.objects.filter
    lookup_field = 'p_id'

    def get(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.queryset(p_id=self.kwargs['p_id'])
        serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
