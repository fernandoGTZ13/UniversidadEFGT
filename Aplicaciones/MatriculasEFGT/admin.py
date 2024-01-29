from django.contrib import admin
#Importa archivo cliente de .models
from .models import AsignaturaEFGT
#Importar
from .models import CursoEFGT

from .models import CarreraEFGT
# Register your models here.
#CRUD
admin.site.register(AsignaturaEFGT)
#Agregar Crud
admin.site.register(CursoEFGT)

admin.site.register(CarreraEFGT)
