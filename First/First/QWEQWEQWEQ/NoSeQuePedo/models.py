from django.db import models

# Create your models here.
class Usuario(models.Model):
        Nombre = models.CharField(max_length=30)
        ApellidoPaterno = models.CharField(max_length=30)
        ApellidoMaterno = models.CharField(max_length=30)
        SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
        Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
        FechaRegistro = models.DateTimeField(auto_now_add=True)



class AñadirUsuarios(models.Model):
    Nombrazo = models.CharField(max_length=31, null=False)
    Apellidos = models.CharField(max_length=30, null=False)
    Email = models.CharField(max_length=50, null=False)
    Contraseña = models.CharField(max_length=30, null=False)
    Edad = models.IntegerField(null=True)
    ultimoAcceso = models.DateTimeField(null=True)
    FechaNac = models.DateField(null=True)
    Ocupacion = models.CharField(max_length=100, null=True)
    Telefono = models.CharField(max_length=20, null=True)
    Ciudad_Origen = models.CharField(max_length=100, null=True)
    Ciudad_Actual = models.CharField(max_length=100, null=True)



class Publicaciones(models.Model):
    msg = models.CharField(max_length=280)
    horaPublic = models.DateTimeField(auto_now_add=True)
    Email = models.CharField(max_length=50, null=True)
