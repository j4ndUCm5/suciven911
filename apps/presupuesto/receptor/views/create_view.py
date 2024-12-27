from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout
from ..forms import ReceptorForm
from ..services import ReceptorService

class ReceptorCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = ReceptorForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Receptor"
        context["titleForm"] = "Añadir un receptor"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("receptor:list")
        context["urlForm"] = reverse_lazy("api_receptor:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

class ReceptorCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ReceptorForm

    def __init__(self):
        self.service = ReceptorService()
