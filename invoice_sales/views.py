from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from product.models import ProductPrice
from .serializers import InvoiceSalesSerializer,\
    InvoiceSalesAddSerializer,\
    InvoiceSalesItemSerializer,\
    InvoiceSalesItemAddSerializer
from .models import InvoiceSales, InvoiceSalesItem
from core.utils import translate
from invoice_customer.models import ProductEntity

# Create your views here.


class InvoiceSalesAddView(GenericAPIView):
    serializer_class = InvoiceSalesAddSerializer
    queryset = InvoiceSales.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceSalesItemAddView(GenericAPIView):
    serializer_class = InvoiceSalesItemAddSerializer
    queryset = InvoiceSales.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        invoice = InvoiceSales.objects.get(id=serializer.data['is_id'])
        product_price = ProductPrice.objects.get(id=serializer.data['p_id'])
        price = product_price.pp_price + (product_price.pp_price * 0.3)
        ProductEntity.objects.create(
            u_store_id_id=invoice.u_store_id.id,
            isi_id_id=invoice.id,
            p_id_id=serializer.data['p_id'],
            isi_price=price,
            sale_price=price,
            pe_weight=serializer.data['isi_weight'],
        )
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceSalesShowAllView(ListAPIView):
    serializer_class = InvoiceSalesSerializer
    queryset = InvoiceSales.objects.all().order_by('-is_date_time')
    filterset_fields = ['u_wholesaler_id', 'u_store_id', 'is_date_time']


class InvoiceSalesShowDetailView(RetrieveAPIView):
    serializer_class = InvoiceSalesSerializer
    queryset = InvoiceSales.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        item_instance = InvoiceSalesItem.objects.filter(is_id_id=serializer.data['id'])
        item_serializer = InvoiceSalesItemSerializer(item_instance, many=True)
        return Response({'invoice': serializer.data, 'items': item_serializer.data}, status.HTTP_200_OK)


class InvoiceSalesShowDetailWholesalerView(GenericAPIView):
    serializer_class = InvoiceSalesSerializer
    queryset = InvoiceSales.objects.all()
    lookup_field = 'u_wholesaler_id'

    def get(self, request: Request, *args, **kwargs):
        translate(request)
        invoice_entry = InvoiceSales.objects.filter(u_wholesaler_id_id=self.kwargs['u_wholesaler_id'])
        serializer = self.serializer_class(invoice_entry, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class InvoiceSalesShowDetailStoreView(GenericAPIView):
    serializer_class = InvoiceSalesSerializer
    queryset = InvoiceSales.objects.all()
    lookup_field = 'u_store_id'

    def get(self, request: Request, *args, **kwargs):
        translate(request)
        invoice_entry = InvoiceSales.objects.filter(u_store_id_id=self.kwargs['u_store_id'])
        serializer = self.serializer_class(invoice_entry, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
