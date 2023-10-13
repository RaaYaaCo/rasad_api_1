from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _

from core.utils import translate
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.request import Request

from .serializers import RatingStoreSerializer, ComplaintSerializer, StoreIdSerializer, UserIdSerializer, \
    RatingViewSerializer, ComplaintDetailSerializer
from .models import RatingStore, Complaint


class RatingStoreAPIView(generics.CreateAPIView):
    queryset = RatingStore.objects.all()
    serializer_class = RatingStoreSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            previous_rate = RatingStore.objects.get(u_customer_id=serializer.validated_data['u_customer_id'],
                                                    u_store_id=request.data['u_store_id'])
            previous_rate.r_id = serializer.validated_data['r_id']
            previous_rate.save()
            serializer.save()
            return Response(data={'data': serializer.data, 'msg': _('your rate registered')},
                            status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
            serializer.save()
            return Response(data={'data': serializer.data, 'msg': _('your rate registered')},
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


class AverageRatingStore(generics.GenericAPIView):
    queryset = RatingStore.objects.filter
    serializer_class = StoreIdSerializer

    def post(self, request: Request):
        instance = self.queryset(u_store_id=request.data['store_id'])
        serializer = RatingStoreSerializer(instance=instance, many=True)
        total_rating = []
        for item in serializer.data:
            total_rating.append(item['r_id'])
        if len(total_rating) == 0:
            return Response({'average_rate': 0}, status.HTTP_200_OK)
        average = sum(total_rating) / len(total_rating)

        return Response({'average_rate': average}, status.HTTP_200_OK)


class RatingShowView(generics.GenericAPIView):
    queryset = RatingStore.objects.get
    serializer_class = RatingViewSerializer

    def post(self, request: Request):
        try:
            instance = self.queryset(u_customer_id=request.data['user_id'],
                                     u_store_id=request.data['store_id'])
            serializer = RatingStoreSerializer(instance=instance, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({'msg': 'this user or store does not exist'}, status=status.HTTP_404_NOT_FOUND)


class ComplaintDetailAPIView(generics.GenericAPIView):
    queryset = Complaint.objects.filter
    serializer_class = ComplaintDetailSerializer

    def post(self, request: Request):
        instance = self.queryset(u_customer_id=request.data['user_id'], u_store_id=request.data['store_id'])
        serializer = ComplaintSerializer(instance=instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


