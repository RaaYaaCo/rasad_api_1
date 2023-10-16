from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import InvoiceEntrySerializer,\
    InvoiceEntryAddSerializer,\
    InvoiceEntryItemSerializer,\
    InvoiceEntryItemAddSerializer
from .models import InvoiceEntry, InvoiceEntryItem
from core.utils import translate

# Create your views here.


class InvoiceEntryAddView(GenericAPIView):
    serializer_class = InvoiceEntryAddSerializer
    queryset = InvoiceEntry.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceEntryItemAddView(GenericAPIView):
    serializer_class = InvoiceEntryItemAddSerializer
    queryset = InvoiceEntryItem.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceEntryShowAllView(ListAPIView):
    serializer_class = InvoiceEntrySerializer
    queryset = InvoiceEntry.objects.all().order_by('-ie_date_time')
    filterset_fields = ['u_wholesaler_id', 'ie_date_time']


class InvoiceEntryShowDetailView(RetrieveAPIView):
    serializer_class = InvoiceEntrySerializer
    queryset = InvoiceEntry.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        item_instance = InvoiceEntryItem.objects.filter(ie_id_id=serializer.data['id'])
        item_serializer = InvoiceEntryItemSerializer(item_instance, many=True)
        return Response({'invoice': serializer.data, 'items': item_serializer.data}, status.HTTP_200_OK)


class InvoiceEntryShowDetailWholesaler(GenericAPIView):
    serializer_class = InvoiceEntrySerializer
    queryset = InvoiceEntry.objects.all()
    lookup_field = 'u_wholesaler_id'

    def get(self, request: Request, *args, **kwargs):
        translate(request)
        invoice_entry = InvoiceEntry.objects.filter(u_wholesaler_id_id=self.kwargs['u_wholesaler_id'])
        serializer = self.serializer_class(invoice_entry, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
