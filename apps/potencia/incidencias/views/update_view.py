from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import IncidenciaForm
from ..models import Incidencia
from ..services import IncidenciaService


class IncidenciaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = IncidenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Potencia"
        context["submodule"] = "Incidencias"
        context["titleForm"] = "Actualizar incidencia"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("incidencias:list")
        context["urlForm"] = reverse_lazy(
            "api_incidencias:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Incidencia.objects.filter(pk=id)


class IncidenciaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = IncidenciaForm

    def __init__(self):
        self.service = IncidenciaService()
