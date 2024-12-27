from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from templates.sneat import TemplateLayout

class Modules(LoginRequiredMixin, TemplateView):
    login_url = "auth:login"
    template_name = "public/modules/index.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["modules"] = [
            {
                "title": "Asesoría Jurídica",
                "url": "denuncias:list",
                "image": "img/gestion_administrativa.png",
            },
            {
                "title": "Emergencias",
                "url": "emergencias:list",
                "image": "img/cuadrantes_de_paz.png",
            },
            {
                "title": "Gestión Administrativa",
                "url": "administracion",
                "image": "img/gestion_administrativa.png",
            },
            {
                "title": "Organización",
                "url": "organizacion",
                "image": "img/organizacion.png",
            },
            {
                "title": "Planificación",
                "url": "planificacion",
                "image": "img/planificacion.png",
            },
            {
                "title": "Presupuesto",
                "url": "presupuesto",
                "image": "img/presupuesto.png",
            },
            {
                "title": "Protección y Seguridad Integral",
                "url": "seguridad",
                "image": "img/seguridad.png",
            },
        ]
        return context
