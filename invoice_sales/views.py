from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import InvoiceSalesSerializer,\
    InvoiceSalesAddSerializer,\
    InvoiceSalesItemSerializer,\
    InvoiceSalesItemAddSerializer
from .models import InvoiceSales, InvoiceSalesItem
from core.utils import translate

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
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceSalesShowAllView(ListAPIView):
    serializer_class = InvoiceSalesSerializer
    queryset = InvoiceSales.objects.all()

    def list(self, request, *args, **kwargs):
        serializers = self.serializer_class(self.get_queryset(), many=True)
        items = []
        for item in serializers.data:
            item_instance = InvoiceSalesItem.objects.filter(is_id_id=item['id'])
            item_serializers = InvoiceSalesItemSerializer(item_instance, many=True)
            print(item_serializers)
            items.append({'invoice': item, 'items': item_serializers.data})
        return Response(items, status.HTTP_200_OK)


class InvoiceSalesShowDetailView(RetrieveAPIView):
    serializer_class = InvoiceSalesSerializer
    queryset = InvoiceSales.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        item_instance = InvoiceSalesItem.objects.filter(is_id_id=serializer.data['id'])
        item_serializer = InvoiceSalesItemSerializer(item_instance, many=True)
        return Response({'invoice': serializer.data, 'items': item_serializer.data}, status.HTTP_200_OK)
