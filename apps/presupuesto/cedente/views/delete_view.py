from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import CedenteForm
from ..models import Cedente
from ..services import CedenteService


class CedenteDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Cedentes"
        context["titleForm"] = "Eliminar cedente"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("cedentes:list")
        context["urlDelete"] = reverse_lazy(
            "api_cedentes:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Cedente.objects.filter(pk=id)


class CedenteDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = CedenteForm

    def __init__(self):
        self.service = CedenteService()
