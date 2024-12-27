import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout

class PresupuestoView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/layout_module.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["module"] = "Presupuesto"
        context["listApiUrl"] = reverse_lazy("api_proyecto:list")
        context["cards"] = self.getCards()
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getCards(self):
        return [
            {
                "title": "Total de Proyectos",
                "subtitle": "Tipo de Proyecto",
                "info": "Proyectos",
                "detail": "00",
                "href": reverse_lazy("proyecto:list"),
            },
                        {
                "title": "Total Acciones",
                "subtitle": "Tipo de Acciones",
                "info": "Accion",
                "detail": "32",
                "href": reverse_lazy("acciones:list"),
            },
            {
                "title": "Total de Asignaciones",
                "subtitle": "Tipo de Asignación",
                "info": "Asignaciones",
                "detail": "32",
                "href": reverse_lazy("asignacion:list"),
            },
            {
                "title": "Total Cedente",
                "subtitle": "Tipo de Cedente",
                "info": "Cedente",
                "detail": "32",
                "href": reverse_lazy("cedente:list"),
            },
            {
                "title": "Total Receptor",
                "subtitle": "Tipo de Receptor",
                "info": "Receptor",
                "detail": "32",
                "href": reverse_lazy("receptor:list"),
            },
        ]

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
                "data": "nombrep",
                "name": "nombrep",
                "title": "Nombre de Proyecto",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fechai",
                "name": "fechai",
                "title": "Fecha de Inicio",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fechac",
                "name": "fechac",
                "title": "Fecha de Culminación",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "situacionp",
                "name": "situacionp",
                "title": "Situacion Presupuestaria",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "montoproyecto",
                "name": "montoproyecto",
                "title": "Monto del Proyecto",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsableg",
                "name": "responsableg",
                "title": "Gerente Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsablet",
                "name": "responsablet",
                "title": "Responsable Técnico",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsabler",
                "name": "responsabler",
                "title": "Registrador Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsablea",
                "name": "responsablea",
                "title": "Administrador Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estatus",
                "name": "estatus",
                "title": "Estatus del Proyecto",
                "orderable": "false",
                "searchable": "false",
            },
        ]