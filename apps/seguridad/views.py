import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout

class SeguridadView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/layout_module.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["module"] = "seguridad"
        context["listApiUrl"] = reverse_lazy("api_entradas:list")
        context["cards"] = self.getCards()
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getCards(self):
        return [
            {
                "title": "Total de Entradas",
                "subtitle": "Tipo de Entradas",
                "info": "Entradas",
                "detail": "00",
                "href": reverse_lazy("entradas:list"),
            },
            {
                "title": "Total de Salidas",
                "subtitle": "Tipo de Salidas",
                "info": "Salidas",
                "detail": "32",
                "href": reverse_lazy("salida:list"),
            },
            {
                "title": "Total Gestiones",
                "subtitle": "Tipo de Gestiones",
                "info": "Gestiones",
                "detail": "32",
                "href": reverse_lazy("gestion:list"),
            },
            {
                "title": "Total Vehiculos",
                "subtitle": "Tipo de vehiculos",
                "info": "Vehiculos",
                "detail": "32",
                "href": reverse_lazy("vehiculo:list"),
            },
        ]

    def getColumns(self):
        return [
            {
                "data": "name",
                "name": "name",
                "title": "Nombre",
                "orderable": "true",
                "searchable": "true",
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
                "data": "telefono",
                "name": "telefono",
                "title": "Teléfono",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fecha",
                "name": "fecha",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "direccion",
                "name": "direccion",
                "title": "Dirección",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cargo",
                "name": "cargo",
                "title": "Cargo",
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