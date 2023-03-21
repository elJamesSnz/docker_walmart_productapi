from django.db import models

class Categoria(models.Model):
    url = models.URLField()

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias')
    name = models.CharField(max_length=200)
    img = models.URLField()
    precio_anterior = models.CharField(max_length=20)
    precio_descuento = models.CharField(max_length=20)