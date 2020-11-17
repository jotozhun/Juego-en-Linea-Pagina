from django.db import models
from datetime import datetime

class Aspecto(models.Model):
    camiseta=models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    rostro= models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

class Partidos(models.Model):
    num_partidos= models.IntegerField(default=0, blank=True, null=True)
    num_partidos_ganados= models.IntegerField(default=0, blank=True, null=True)
    num_partidos_perdidos= models.IntegerField(default=0, blank=True, null=True)
    goles_anotados=models.IntegerField(default=0, blank=True, null=True)
    goles_atajados=models.IntegerField(default=0, blank=True, null=True)
    goles_recibidos= models.IntegerField(default=0, blank=True, null=True)
    posicion_ranking= models.IntegerField(default=0, blank=True, null=True)

class RegistroTorneo(models.Model):
    registrado=models.BooleanField()

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contraseña= models.CharField( max_length=50)
    partido = models.ForeignKey(Partidos, null = False, on_delete=models.CASCADE)
    aspecto = models.ForeignKey(Aspecto, null =False, on_delete=models.CASCADE)
    registro= models.ForeignKey(RegistroTorneo, null = False, on_delete=models.CASCADE)
        
class ReglaTorneo(models.Model):
    num_goles=models.IntegerField(default=0, blank=True, null=True)
    tiempo_espera = models.TimeField((""), auto_now=False, auto_now_add=False)
    tiempo_patear = models.TimeField((""), auto_now=False, auto_now_add=False)

class InicioTorneo(models.Model):
    fecha_inicio = models.DateField(default=datetime.now, blank=True)
    fecha_fin = models.DateField(default=datetime.now, blank=True)
    num_participantes=models.IntegerField(default=0, blank=True, null=True)
    hora_inicio = models.TimeField((""), auto_now=False, auto_now_add=False)

class Premios(models.Model):
    nombre_premio=models.CharField(max_length=50)
    sponsor_premio=models.CharField(max_length=50)
    descripcion_premio= models.CharField(max_length=50)
    imagen_premio=models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    cantidad_unidades= models.IntegerField()

class Torneo(models.Model):
    reglas= models.ForeignKey(ReglaTorneo, null =False, on_delete=models.CASCADE)
    premios = models.ForeignKey(Premios, null = False, on_delete=models.CASCADE)
    inicio = models.ForeignKey(InicioTorneo, null = False, on_delete=models.CASCADE)
    nombre_Torneo=models.CharField(max_length=50)
    
class Grupos(models.Model):
    num_grupos=models.IntegerField(default=0, blank=True, null=True)

class Juego(models.Model):
    publicidad = models.CharField( max_length=50)
    tipografia = models.CharField( max_length=50)
    imagen = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    musica = models.CharField( max_length=50)