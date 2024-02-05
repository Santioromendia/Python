from django.db import models

# Create your models here.

class pais (models.Model):
    nombre= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class cliente(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    nacimiento= models.DateField(null=True, blank=True)
    pais_origen_id=models.ForeignKey(pais, null=True, blank=True, on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    