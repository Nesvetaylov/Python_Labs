from django.urls import path, include
from django.contrib import admin
from .views import add_client, clients_list

urlpatterns = [
    path('', add_client, name='add_client'),
    path('clients/', clients_list, name='clients_list'),
    path('admin/', admin.site.urls),
    path('', include('clients.urls')),
]