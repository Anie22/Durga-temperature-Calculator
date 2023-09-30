from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import temperature_converter, convert_temperature, conversion_history, register, login_view, logout_view, delete, delete_all

app_name = "home"

urlpatterns = [
    path('', login_required(temperature_converter), name='temperature_converter'),
    path('convert_temperature/', convert_temperature, name='convert_temperature'),
    path('history/', conversion_history, name='history'),
    path('account/signup/', register, name='register'),
    path('account/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('delete/<int:id>/', delete, name='delete'),
    path('delete/', delete_all, name='delete_all')
]