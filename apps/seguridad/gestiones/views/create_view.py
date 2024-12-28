from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout
from ..forms import GestionForm
from ..services import GestionService

class GestionCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = GestionForm
    template_name = "sneat/layout/partials/form/layout_gestion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Gestion"
        context["titleForm"] = "Añadir una gestion nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("gestion:list")
        context["urlForm"] = reverse_lazy("api_gestion:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

class GestionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = GestionForm

    def __init__(self):
        self.service = GestionService()
