from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout
from ..forms import SalidaForm
from ..services import SalidaService

class SalidaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = SalidaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Salida"
        context["titleForm"] = "Añadir una salida nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("salida:list")
        context["urlForm"] = reverse_lazy("api_salida:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

class SalidaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = SalidaForm

    def __init__(self):
        self.service = SalidaService()
