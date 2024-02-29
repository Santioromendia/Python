from django.db import models

# Create your models here.

class pais (models.Model):
    nombre= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class sede (models.Model):
    sede= models.CharField(max_length=100)
    
    def __str__(self):
        return self.sede
    
class cliente(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    nacimiento= models.DateField(null=True, blank=True)
    pais_origen=models.ForeignKey(pais, null=True, blank=True, on_delete=models.SET_NULL)
    ciudad=models.CharField(max_length=100, null=True, blank=True)
    peso=models.FloatField(null=True, blank=True)
    altura=models.FloatField(null=True, blank=True)
    telefono=models.FloatField(null=True, blank=True)
    mail=models.EmailField(max_length=254, null=True, blank=True)
    sede=models.ForeignKey(sede, null=True, blank=True, on_delete=models.SET_NULL)
    
   
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    