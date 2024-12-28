from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

class Receptor(BaseModel):
    idr = models.CharField(max_length=100, verbose_name="Id Receptor:", default="")
    partidar = models.CharField(max_length=64, verbose_name="Partida", default="")
    generalr = models.CharField(max_length=64, verbose_name="General", default="")
    espefr = models.CharField(max_length=64, verbose_name="Específicaciones", default="")
    subespefr = models.CharField(max_length=64, verbose_name="Sub-Especialidad", default="")
    denomr = models.CharField(max_length=64, verbose_name="Denomincación", default="")
    presuacorr = models.CharField(max_length=64, verbose_name="Presupuesto acordado", default="")
    caufechar = models.CharField(max_length=64, verbose_name="Causado a la fecha", default="")
    dispr = models.CharField(max_length=64, verbose_name="Disponible a causar", default="")
    montocr = models.CharField(max_length=64, verbose_name="Monto", default="")
    saldofr = models.CharField(max_length=64, verbose_name="Saldo final", default="")
    direccionr = models.CharField(max_length=64, verbose_name="Dirección receptora", default="")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.partidar, self.generalr)

    class Meta:
        verbose_name = "Receptor"
        verbose_name_plural = "Receptores"
