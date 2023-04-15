from django.db import models

# Create your models here.
class Vendedor(models.Model):
    vendedor = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField()

class Producto(models.Model):
    identificador = models.IntegerField()
    producto = models.CharField(max_length=50)

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    email = models.EmailField()
    inscripcion = models.DateField()