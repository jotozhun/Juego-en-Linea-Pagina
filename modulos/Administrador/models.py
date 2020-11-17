from django.db import models

class aspecto(models.Model):
    camiseta=models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    rostro= models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

class partidos(models.Model):
    num_partidos= models.IntegerField()
    num_partidos_ganados= models.IntegerField()
    num_partidos_perdidos= models.IntegerField()
    goles_anotados=models.IntegerField()
    goles_atajados=models.IntegerField()
    goles_recibidos= models.IntegerField()
    posicion_ranking= models.IntegerField()

class registroTorneo(models.Model):
    registrado=models.BooleanField()

class torneo(models.Model):
    reglas= models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    premios = models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    nombre_Torneo=models.CharField(max_length=50)

class jugador(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contraseña= models.CharField( max_length=50)
        
class reglaTorneo(models.Model):
    num_goles=models.IntegerField()
    tiempo_espera = models.TimeField((""), auto_now=False, auto_now_add=False)
    tiempo_patear = models.TimeField((""), auto_now=False, auto_now_add=False)

class inicioTorneo(models.Model):
    fecha_inicio = models.DateField((""), auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField((""), auto_now=False, auto_now_add=False)
    num_participantes=models.IntegerField()
    hora_inicio = models.TimeField((""), auto_now=False, auto_now_add=False)

class Premios(models.Model):
    nombre_premio=models.CharField((""), max_length=50)
    sponsor_premio=models.CharField((""), max_length=50)
    descripcion_premio= models.CharField((""), max_length=50)
    imagen_premio=models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    cantidad_unidades= models.IntegerField((""))

class Grupos(models.Model):
    num_grupos=models.IntegerField((""))

class Juego(models.Model):
    publicidad = models.CharField((""), max_length=50)
    tipografia = models.CharField((""), max_length=50)
    imagen = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    musica = models.CharField((""), max_length=50)