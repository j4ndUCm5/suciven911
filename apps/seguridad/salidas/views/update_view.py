from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from templates.sneat import TemplateLayout
from ..forms import SalidaForm
from ..models import Salida
from ..services import SalidaService

class SalidaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = SalidaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Salida"
        context["titleForm"] = "Actualizar salida"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("salida:list")
        context["urlForm"] = reverse_lazy("api_salida:update", args=[self.kwargs.get("pk")])
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Salida.objects.filter(pk=id)

class SalidaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = SalidaForm

    def __init__(self):
        self.service = SalidaService()
