from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout
from ..forms import AsignacionForm
from ..services import AsignacionService

class AsignacionCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = AsignacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Asignaciones"
        context["titleForm"] = "Añadir una asignacion"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("asignaciones:list")
        context["urlForm"] = reverse_lazy("api_asignaciones:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

class AsignacionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = AsignacionForm

    def __init__(self):
        self.service = AsignacionService()
