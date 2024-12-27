import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import ReceptorService

class ReceptorListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Receptor"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("receptor:create")
        context["listApiUrl"] = reverse_lazy("api_receptor:list")
        context["updateUrl"] = reverse_lazy("receptor:update", args=[0])
        context["deleteUrl"] = reverse_lazy("receptor:delete", args=[0])
        context["exportPdfUrl"] = reverse_lazy("api_receptor:export_pdf")
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "idr",
                "name": "idr",
                "title": "ID Receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "partidar",
                "name": "partidar",
                "title": "Partida receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "generalr",
                "name": "generalr",
                "title": "General receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "espefr",
                "name": "espefr",
                "title": "Específicaciones receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "subespefr",
                "name": "subespefr",
                "title": "Sub-especialidad",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "denomr",
                "name": "denomr",
                "title": "Denominacion Receptor",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "presuacorr",
                "name": "presuacorr",
                "title": "Presupuesto acordado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "caufechar",
                "name": "caufechar",
                "title": "Causado a la fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "dispr",
                "name": "dispr",
                "title": "Disponible a causar",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "montocr",
                "name": "montocr",
                "title": "Monto a receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "saldofr",
                "name": "saldofr",
                "title": "Saldo final",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "direccionr",
                "name": "direccionr",
                "title": "Dirección receptora",
                "orderable": "false",
                "searchable": "false",
            },
        ]

class ReceptorListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = ReceptorService()
