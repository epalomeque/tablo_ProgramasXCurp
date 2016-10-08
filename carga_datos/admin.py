from django.contrib import admin
from carga_datos.models import cat_programas,curp_mas_cvprograma,archivo

# Register your models here.
admin.site.register(cat_programas)
admin.site.register(curp_mas_cvprograma)
admin.site.register(archivo)