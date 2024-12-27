from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from templates.sneat import TemplateLayout
from ..forms import VehiculoForm
from ..models import Vehiculo
from ..services import VehiculoService

class VehiculoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Vehiculo"
        context["titleForm"] = "Eliminar vehiculo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("vehiculo:list")
        context["urlDelete"] = reverse_lazy("api_vehiculo:delete", args=[self.kwargs.get("pk")])
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Vehiculo.objects.filter(pk=id)

class VehiculoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = VehiculoForm

    def __init__(self):
        self.service = VehiculoService()
