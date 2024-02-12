from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from vehicle.models import Car, Moto, Milage
from vehicle.paginators import VehiclePagination
from vehicle.permissions import IsOwnerOrStaff
from vehicle.serializers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, \
    MotoCreateSerializer
from rest_framework.permissions import IsAuthenticated


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]


# class MotoCreateAPIView(generics.CreateAPIView):
#     serializer_class = MotoSerializer


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    pagination_class = VehiclePagination


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = [IsOwnerOrStaff]


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer


class MilageListAPIView(generics.ListAPIView):
    serializer_class = MilageSerializer
    queryset = Milage.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto',)
    ordering_fields = ('year',)


class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer
