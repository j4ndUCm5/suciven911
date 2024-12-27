from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import SedeForm
from ..models import Sede
from ..services import SedeService


class SedeUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = SedeForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Sedes"
        context["titleForm"] = "Actualizar sede"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("sedes:list")
        context["urlForm"] = reverse_lazy(
            "api_sedes:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Sede.objects.filter(pk=id)


class SedeUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = SedeForm

    def __init__(self):
        self.service = SedeService()
