from django.urls import path
from .views import temperature_converter, convert_temperature

urlpatterns = [
    path('temperature_converter/', temperature_converter, name='temperature_converter'),
    path('convert_temperature/', convert_temperature, name='convert_temperature'),
]