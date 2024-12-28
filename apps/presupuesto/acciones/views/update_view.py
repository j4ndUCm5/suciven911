from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from templates.sneat import TemplateLayout
from ..forms import AccionForm
from ..models import Accion
from ..services import AccionService

class AccionUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = AccionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Accion"
        context["titleForm"] = "Actualizar accion"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("acciones:list")
        context["urlForm"] = reverse_lazy(
            "api_accion:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Accion.objects.filter(pk=id)

class AccionUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = AccionForm

    def __init__(self):
        self.service = AccionService()
