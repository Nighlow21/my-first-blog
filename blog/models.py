from django.db import models

class Post(models.Model):
    tcar = models.CharField(max_length=150)  # Tipo de Carne
    tbe = models.CharField(max_length=150)   # Tipo de Bebida
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='https://i.blogs.es/5fc93e/1/1366_2000.jpg')

    def __str__(self):
        return self.nombre
