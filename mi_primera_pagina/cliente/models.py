from django.db import models

class pais(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name="pais"
        verbose_name_plural = "países"
        
class comida(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
      
class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True) #no es obligatorio
    pais_origen_id = models.ForeignKey(pais, null=True, blank=True, on_delete=models.SET_NULL)
    comida_id = models.ForeignKey(comida, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    

