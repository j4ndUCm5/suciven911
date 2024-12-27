import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout

class PlanificacionView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/layout_module.html"
    
    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["module"] = "Planificación"
        context["listApiUrl"] = reverse_lazy("api_objetivos:list")
        context["cards"] = self.getCards()
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getCards(self):
        return [
            {
                "title": "Total de Objetivos",
                "info": "Objetivos",
                "detail": "02",
                "href": reverse_lazy("objetivos:list"),
            },
            {
                "title": "Total de Actividades",
                "info": "Actividades",
                "detail": "02",
                "href": reverse_lazy("actividades:list"),
            },
            {
                "title": "Total de Llamadas",
                "info": "LLamadas",
                "detail": "02",
                "href": reverse_lazy("llamadas:list"),
            },
            {
                "title": "Total de Infraestructuras",
                "info": "Infraestructuras",
                "detail": "02",
                "href": reverse_lazy("infraestructuras:list"),
            },
            {
                "title": "Total de Transportes",
                "info": "Transportes",
                "detail": "02",
                "href": reverse_lazy("transportes:list"),
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
                    "data": "fechai",
                    "name": "fechai",
                    "title": "Fecha Inicial",
                    "orderable": "false",
                    "searchable": "false",
                },
                {
                    "data": "fechaf",
                    "name": "fechaf",
                    "title": "Fecha Final",
                    "orderable": "false",
                    "searchable": "false",
                },
                {
                    "data": "objetiv",
                    "name": "objetiv",
                    "title": "Objetivo",
                    "orderable": "false",
                    "searchable": "false",
                },
                {
                    "data": "meta",
                    "name": "meta",
                    "title": "Meta",
                    "orderable": "false",
                    "searchable": "false",
                },
            ]  