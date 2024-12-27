import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import RegistroFilmicoService


class RegistroFilmicoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Registro Filmico"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("filmicos:create")
        context["listApiUrl"] = reverse_lazy("api_filmicos:list")
        context["updateUrl"] = reverse_lazy("filmicos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("filmicos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_filmicos:export_excel")
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "estatus",
                "name": "estatus",
                "title": "Estatus",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "direccion",
                "name": "direccion",
                "title": "Direccion",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "camara",
                "name": "camara",
                "title": "Camara",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "motivo_solicitud",
                "name": "motivo_solicitud",
                "title": "Motivo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "ente_solicita",
                "name": "ente_solicita",
                "title": "Ente",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "fecha_solicitud",
                "name": "fecha_solicitud",
                "title": "Fecha de solicitud",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class RegistroFilmicoListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = RegistroFilmicoService()
