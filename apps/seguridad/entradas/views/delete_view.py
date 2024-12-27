from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from ..forms import EntradaForm
from ..models import Entrada
from ..services import EntradaService
from templates.sneat import TemplateLayout

class EntradaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Entradas"
        context["titleForm"] = "Eliminar entrada"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("entradas:list")
        context["urlDelete"] = reverse_lazy("api_entradas:delete", args=[self.kwargs.get("pk")] )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Entrada.objects.filter(pk=id)

class EntradaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = EntradaForm

    def __init__(self):
        self.service = EntradaService()
