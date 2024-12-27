from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from templates.sneat import TemplateLayout
from ..forms import VehiculoForm
from ..models import Vehiculo
from ..services import VehiculoService

class VehiculoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = VehiculoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Vehiculo"
        context["titleForm"] = "Actualizar vehiculo"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("vehiculo:list")
        context["urlForm"] = reverse_lazy("api_vehiculo:update", args=[self.kwargs.get("pk")])
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Vehiculo.objects.filter(pk=id)

class VehiculoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = VehiculoForm

    def __init__(self):
        self.service = VehiculoService()
