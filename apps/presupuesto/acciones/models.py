from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

class Accion(BaseModel):
    nombrep = models.CharField(max_length=64, verbose_name="Nombre del Proyecto:")
    fechai = models.DateField(verbose_name="Fecha de Inicio")
    fechac = models.DateField(verbose_name="Fecha de Culminación")
    situacionp = models.CharField( max_length=64, verbose_name="Situación Presupuestaria:")
    montoproyecto = models.CharField( max_length=64, verbose_name="Monto Total del Proyecto:" )
    responsableg = models.CharField(max_length=64, verbose_name="Responsable Gerente:")
    responsablet = models.CharField(max_length=64, verbose_name="Responsable Técnico:")
    responsabler = models.CharField(max_length=64, verbose_name="Responsable Registrador:"  )
    responsablea = models.CharField( max_length=64, verbose_name="Responsable Administrativo:"  )
    estatus = models.CharField(max_length=64, verbose_name="Estatus del Proyecto:")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombrep

    class Meta:
        verbose_name = "Accion"
        verbose_name_plural = "Acciones"
        app_label = 'presupuesto'
