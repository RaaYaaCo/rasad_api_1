from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .serializers import InvoiceCustomerAddSerializer, InvoiceCustomerItemAddSerializer
from .models import InvoiceCustomer, InvoiceCustomerItem
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
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
