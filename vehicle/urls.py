from django.urls import path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView, \
    MotoDestroyAPIView, MilageCreateAPIView, MotoMilageListAPIView, MilageListAPIView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto_create'),
    path('moto/', MotoListAPIView.as_view(), name='moto_list'),
    path('moto/<int:pk>/', MotoRetrieveAPIView.as_view(), name='moto_detail'),
    path('moto/update/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto_update'),
    path('moto/delete/<int:pk>/', MotoDestroyAPIView.as_view(), name='moto_delete'),

    path('milage/create/', MilageCreateAPIView.as_view(), name='milage_create'),
    path('milage/', MilageListAPIView.as_view(), name='milage_list'),
    path('moto/milage/', MotoMilageListAPIView.as_view(), name='moto_milage_list'),
] + router.urls
