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
    queryset = InvoiceEntry.objects.all()

    def list(self, request, *args, **kwargs):
        serializers = self.serializer_class(self.get_queryset(), many=True)
        items = []
        for item in serializers.data:
            item_instance = InvoiceEntryItem.objects.filter(ie_id_id=item['id'])
            item_serializers = InvoiceEntryItemSerializer(item_instance, many=True)
            print(item_serializers)
            items.append({'invoice': item, 'items': item_serializers.data})
        return Response(items, status.HTTP_200_OK)


class InvoiceEntryShowDetailView(RetrieveAPIView):
    serializer_class = InvoiceEntrySerializer
    queryset = InvoiceEntry.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        item_instance = InvoiceEntryItem.objects.filter(ie_id_id=serializer.data['id'])
        item_serializer = InvoiceEntryItemSerializer(item_instance, many=True)
        return Response({'invoice': serializer.data, 'items': item_serializer.data}, status.HTTP_200_OK)
