from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import InvoiceEntrySerializer, InvoiceEntryItemSerializer
from .models import InvoiceEntry, InvoiceEntryItem
from core.utils import translate

# Create your views here.


class InvoiceEntryAddView(GenericAPIView):
    serializer_class = InvoiceEntrySerializer
    queryset = InvoiceEntry.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceEntryItemAddView(GenericAPIView):
    serializer_class = InvoiceEntryItemSerializer
    queryset = InvoiceEntryItem.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
