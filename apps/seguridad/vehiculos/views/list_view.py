import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import VehiculoService

class VehiculoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
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
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "ID",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "nombre",
                "name": "nombre",
                "title": "Nombre",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "apellido",
                "name": "apellido",
                "title": "Apellido",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cedula",
                "name": "cedula",
                "title": "Cédula",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "modelo",
                "name": "modelo",
                "title": "Modelo",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "vehiculo",
                "name": "vehiculo",
                "title": "Vehículo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "motivo",
                "name": "motivo",
                "title": "Motivo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "capagasolina",
                "name": "capagasolina",
                "title": "Capacidad de gasolina",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cantigasolina",
                "name": "cantigasolina",
                "title": "Cantidad de gasolina",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "placa",
                "name": "placa",
                "title": "Placa",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fecha",
                "name": "fecha",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "hora",
                "name": "hora",
                "title": "Hora",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class VehiculoListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = VehiculoService()
