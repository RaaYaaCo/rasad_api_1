from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from .serializers import InvoiceCustomerAddSerializer,\
    InvoiceCustomerItemAddSerializer,\
    InvoiceCustomerSerializer,\
    InvoiceCustomerItemSerializer
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
                return Response({'msg': 'Requested weight is not available'}, status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except:
            return Response({'msg': 'error!!'}, status.HTTP_400_BAD_REQUEST)


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
