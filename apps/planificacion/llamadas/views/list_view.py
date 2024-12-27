import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from ..models import Llamada

from templates.sneat import TemplateLayout

from ..services import LlamadaService

class LlamadaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/llamadas.html"

    def get_context_data(self, **kwargs):
        columns = Llamada.objects.all()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Llamadas"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("llamadas:create")
        context["listApiUrl"] = reverse_lazy("api_llamadas:list")
        context["updateUrl"] = reverse_lazy("llamadas:update", args=[0])
        context["deleteUrl"] = reverse_lazy("llamadas:delete", args=[0])
        context["heads"] = columns
        context["columns"] = columns
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
                "data": "mes",
                "name": "mes",
                "title": " Mes",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estado",
                "name": "estado",
                "title": "Estado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "informativa",
                "name": "informativa",
                "title": "LLamadas informativas",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "falsa",
                "name": "falsa",
                "title": "Llamadas Falsas",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "realesno",
                "name": "realesno",
                "title": "Llamadas Reales No Efectivas",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "realesf",
                "name": "realesf",
                "title": "Llamadas Reales Efectivas",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "videop",
                "name": "videop",
                "title": "Video Protección",
                "orderable": "false",
                "searchable": "false",
            },
        ]

class LlamadaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = LlamadaService()
