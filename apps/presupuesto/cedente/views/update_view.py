from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from templates.sneat import TemplateLayout
from ..forms import CedenteForm
from ..models import Cedente
from ..services import CedenteService

class CedenteUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = CedenteForm
    template_name = "sneat/layout/partials/form/layout_cedente_editar.html"

    def get_context_data(self, **kwargs):
        id = self.kwargs.get("pk")
        data = Cedente.objects.filter(pk=id).all
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Cedentes"
        context["titleForm"] = "Actualizar cedente"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("cedente:list")
        context["urlForm"] = reverse_lazy(
            "api_cedente:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        context["formu"] = data
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Cedente.objects.filter(pk=id)

class CedenteUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = CedenteForm

    def __init__(self):
        self.service = CedenteService()
