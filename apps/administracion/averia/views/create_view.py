from administracion.averia.forms import AveriaForm
from administracion.averia.services import AveriaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class AveriaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = AveriaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administracion"
        context["submodule"] = "Averia"
        context["titleForm"] = "Añadir una Averia"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("averias:list")
        context["urlForm"] = reverse_lazy("api_averias:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class AveriaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = AveriaForm

    def __init__(self):
        self.service = AveriaService()
