from core.utils import translate
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.request import Request

from .serializers import RatingStoreSerializer, ComplaintSerializer, StoreIdSerializer, UserIdSerializer
from .models import RatingStore, Complaint


class RatingStoreAPIView(generics.CreateAPIView):
    queryset = RatingStore.objects.all()
    serializer_class = RatingStoreSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'data': serializer.data, 'msg': 'your grade has been registered successfully '},
                        status=status.HTTP_201_CREATED)


class ComplaintView(generics.CreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def create(self, request: Request, *args, **kwargs):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ComplaintDetailView(generics.ListAPIView):
    queryset = Complaint.objects.all()

    def list(self, request: Request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = ComplaintSerializer(instance=queryset, many=True)
        return Response(serializer_class.data)


class ComplaintDetailUser(generics.GenericAPIView):
    queryset = Complaint.objects.filter
    serializer_class = UserIdSerializer

    def post(self, request: Request):
        user_id = request.data['user_id']
        instance = self.queryset(u_customer_id=user_id)
        serializer = ComplaintSerializer(instance=instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ComplaintDetailStore(generics.GenericAPIView):
    queryset = Complaint.objects.filter
    serializer_class = StoreIdSerializer

    def post(self, request: Request):
        store_id = request.data['store_id']
        instance = self.queryset(u_store_id=store_id)
        serializer = ComplaintSerializer(instance=instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)









