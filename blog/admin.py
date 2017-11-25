from django.contrib import admin
from .models import Menu,Plato, MenuAdmin,PlatoAdmin
#Registramos nuestras clases principales.

admin.site.register(Menu,MenuAdmin)
admin.site.register(Plato,PlatoAdmin)
# Register your models here.
