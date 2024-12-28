import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import VehiculoService
from ..models import Vehiculo

class VehiculoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/vehiculo.html"

    def get_context_data(self, **kwargs):
        columns = Vehiculo.objects.all()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Vehiculo"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("vehiculo:create")
        context["listApiUrl"] = reverse_lazy("api_vehiculo:list")
        context["updateUrl"] = reverse_lazy("vehiculo:update", args=[0])
        context["deleteUrl"] = reverse_lazy("vehiculo:delete", args=[0])
        context["heads"] = columns
        context["columns"] = columns
        return TemplateLayout.init(self, context)

class VehiculoListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = VehiculoService()
