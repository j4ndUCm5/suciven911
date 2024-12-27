import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import CedenteService

class CedenteListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Cedente"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("cedente:create")
        context["listApiUrl"] = reverse_lazy("api_cedente:list")
        context["updateUrl"] = reverse_lazy("cedente:update", args=[0])
        context["deleteUrl"] = reverse_lazy("cedente:delete", args=[0])
        context["exportPdfUrl"] = reverse_lazy("api_cedente:export_pdf")
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "idc",
                "name": "idc",
                "title": "Identificador Cedente",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "partidac",
                "name": "partidac",
                "title": "Número de Partida",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "generalc",
                "name": "generalc",
                "title": "General",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "espefc",
                "name": "espefc",
                "title": "Específicaciones",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "subespefc",
                "name": "subespefc",
                "title": "Sub-Especialidad",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "denomc",
                "name": "denomc",
                "title": "Denominación cedente",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "presuacorc",
                "name": "presuacorc",
                "title": "Presupuesto Acordado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "caufechac",
                "name": "caufechac",
                "title": "Causado a la Fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "dispc",
                "name": "dispc",
                "title": "Disponible a Causar",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "montocc",
                "name": "montocc",
                "title": "Monto a Ceder",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "saldofc",
                "name": "saldofc",
                "title": "Saldo Final",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "direccionc",
                "name": "direccionc",
                "title": "Dirección Cedente",
                "orderable": "false",
                "searchable": "false",
            },
        ]

class CedenteListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = CedenteService()
