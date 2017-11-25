from django.db import models
from django.contrib import admin

class Plato(models.Model):
    nombre  = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    nombre    = models.CharField(max_length=60)
    platos   = models.ManyToManyField(Plato, through='MenuPlato')
    nombrevendedor  = models.CharField(max_length=30)
    nombrecliente = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Menuplato(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class MenuplatoInLine(admin.TabularInline):
    model = Menuplato
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (MenuplatoInLine,)

class MenuAdmin (admin.ModelAdmin):
    inlines = (MenuplatoInLine,)

# Create your models here.
