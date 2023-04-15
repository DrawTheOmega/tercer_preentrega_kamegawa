from django.urls import path
from Appcoder import views

urlpatterns = [

    path("", views.inicioApp, name="inicio"),
    path("vendedores", views.vendedores, name="Vendedor"),
    path("productos", views.productos, name="Productos")
]