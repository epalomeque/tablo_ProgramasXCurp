from django.db import models

# Create your models here.
class cat_programas(models.Model):
    cv_prog = models.CharField (max_length=10)
    nombre_prog = models.CharField(max_length=80)
    descrip_prog = models.TextField (default='')

    def __unicode__(self):  # __str__ en Python 3
        return self.nombre

class curp_mas_cvprograma(models.Model):
    curp = models.CharField(max_length=18)
    cvprograma = models.ForeignKey(cat_programas)

    def __unicode__(self):  # __str__ en Python 3
        return '%s %s' % (self.curp, self.cvprograma)