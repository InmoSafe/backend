from django.db import models

# Create your models here.
class Inmueble(models.Model):
    apto = models.IntegerField()
    unidad = models.CharField(max_length=100)
    torre = models.IntegerField(null=True)
    ciudad = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    destinacion = models.CharField(max_length=100)
    habitaciones = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    extras = models.TextField(null=True)
    llaves = models.CharField(max_length=100, default='Sin definir')
    link = models.URLField(null=True)
    bono = models.CharField(max_length=100,default='', null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    def __str__(self):
        return self.apto + ' ' + self.unidad