from django.db import models

# Create your models here.


## Proyecto (str)  ## Etapa (str)  # Sector (str)  #Unidad (number)  # Cliente (str)  # F. inspeccion (timestamp) #  FR. Municipal  
# Dias abierto (int)  ##Estado (str)


class Seguimiento(models.Model):
    proyecto = models.CharField(max_length=100, null=True)
    etapa = models.CharField(max_length=100, null=True)
    sector = models.CharField(max_length=100, null=True)
    unidad = models.CharField(null=True, max_length=100)
    cliente = models.CharField(primary_key=True, max_length=100)
    finspeccion = models.DateField(null=True)
    frmunicipal = models.DateField(null=True)
    fvconstructor = models.DateField(null=True)
    dias = models.IntegerField(null=True)
    estado = models.CharField(max_length=100, null=True)

