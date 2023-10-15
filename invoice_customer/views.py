from django.utils.translation import gettext as _

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, GenericAPIView

from .serializers import InvoiceCustomerAddSerializer,\
    InvoiceCustomerItemAddSerializer,\
    InvoiceCustomerSerializer,\
    InvoiceCustomerItemSerializer, \
    ProductEntitySerializer
from .models import InvoiceCustomer, InvoiceCustomerItem, ProductEntity
from core.utils import translate

# Create your views here.


class InvoiceCustomerAddView(CreateAPIView):
    serializer_class = InvoiceCustomerAddSerializer
    queryset = InvoiceCustomer.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceCustomerItemAddView(CreateAPIView):
    serializer_class = InvoiceCustomerItemAddSerializer
    queryset = InvoiceCustomerItem.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(request)
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
            serializer.save()
            invoice = ProductEntity.objects.get(id=serializer.data['pe_id'])
            if invoice.pe_weight >= serializer.data['ici_weight']:
                invoice.pe_weight = invoice.pe_weight - serializer.data['ici_weight']
                invoice.save()
            else:
                return Response({'msg': _('Requested weight is not available')}, status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except:
            return Response({'msg': _('error!!')}, status.HTTP_400_BAD_REQUEST)


class InvoiceCustomerShowAllView(ListAPIView):
    serializer_class = InvoiceCustomerSerializer
    queryset = InvoiceCustomer.objects.all()

    def list(self, request, *args, **kwargs):
        serializers = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializers.data, status.HTTP_200_OK)


class InvoiceCustomerShowDetailView(RetrieveAPIView):
    serializer_class = InvoiceCustomerSerializer
    queryset = InvoiceCustomer.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        item_instance = InvoiceCustomerItem.objects.filter(ic_id_id=serializer.data['id'])
        item_serializer = InvoiceCustomerItemSerializer(item_instance, many=True)
        return Response({'invoice': serializer.data, 'items': item_serializer.data}, status.HTTP_200_OK)


class ProductEntityUpdatePriceView(RetrieveUpdateAPIView):
    serializer_class = ProductEntitySerializer
    queryset = ProductEntity.objects.all()

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object())
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        translate(request)
        serializer = self.serializer_class(instance=self.get_object(), data=request.data)
        serializer.is_valid()
        product_entity = ProductEntity.objects.get(id=serializer.data['id'])
        if int(serializer.data['isi_price']) > int(request.data['sale_price']):
            product_entity.pe_is_active = False
            product_entity.save()
            ProductEntity.objects.create(
                u_store_id_id=product_entity.u_store_id.id,
                isi_id_id=product_entity.isi_id.id,
                p_id_id=product_entity.p_id.id,
                isi_price=product_entity.isi_price,
                sale_price=request.data['sale_price'],
                pe_weight=product_entity.pe_weight,
            )
        else:
            return Response({'msg': _('You are not allowed to increase the price')}, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)


class ProductEntityShowStoreView(GenericAPIView):
    serializer_class = ProductEntitySerializer
    queryset = ProductEntity.objects.all()
    lookup_field = 'u_store_id'

    def get(self, request: Request, *args, **kwargs):
        translate(request)
        product_entity = ProductEntity.objects.filter(u_store_id_id=self.kwargs['u_store_id'])
        serializer = ProductEntitySerializer(product_entity, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class ProductEntityDetailView(RetrieveAPIView):
    serializer_class = ProductEntitySerializer
    queryset = ProductEntity.objects.all()

    def retrieve(self, request, *args, **kwargs):
        translate(request)
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data, status.HTTP_200_OK)
