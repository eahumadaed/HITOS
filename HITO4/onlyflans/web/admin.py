from django.contrib import admin
from .models import Flan, ContacForm, CategoriasProducto


#Registro de modelos en el Administrador
admin.site.register(Flan)
admin.site.register(ContacForm)
admin.site.register(CategoriasProducto)