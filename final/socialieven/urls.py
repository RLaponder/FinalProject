from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('activiteiten', views.activiteiten, name='activiteiten'),
    path('nieuwe_activiteit', views.nieuwe_activiteit, name='nieuwe activiteit')
]