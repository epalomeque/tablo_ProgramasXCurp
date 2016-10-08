from django.db import models

# Create your models here.

class archivo(models.Model):
    nombre_archivo = models.CharField(max_length=100)
    ubicacion_archivo = models.FileField(upload_to='documents/%Y/%m/%d')

class cat_programas(models.Model):
    cv_prog = models.CharField (max_length=10, verbose_name='Clave del Programa')
    nombre_prog = models.CharField(max_length=80, verbose_name='Nombre del Programa')
    descrip_prog = models.TextField (default='', blank=True, verbose_name='Descripcion del Programa')

    def __unicode__(self):  # __str__ en Python 3
        return self.nombre_prog

class curp_mas_cvprograma(models.Model):
    curp = models.CharField(max_length=18, verbose_name='CURP')
    cvprograma = models.ForeignKey(cat_programas, verbose_name='Clave del Programa')

    def __unicode__(self):  # __str__ en Python 3
        return '%s %s' % (self.curp, self.cvprograma)