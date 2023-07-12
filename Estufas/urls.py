from django.urls import path
from . import views

urlpatterns = [
    path('', views.estufas, name='Estufas'),
    path('<int:id>', views.estufa_detalle, name='estufa_detalle'),
]
