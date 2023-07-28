from django.db import models
class product(models.Model):
    categoria = models.TextField()
    nombre= models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen=models.ImageField()
    stock= models.IntegerField()
    
    