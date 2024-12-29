from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from templates.sneat import TemplateLayout
from ..forms import AsignacionForm
from ..models import Asignacion
from ..services import AsignacionService

class AsignacionDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Asignacion"
        context["titleForm"] = "Eliminar asignacion"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("asignacion:list")
        context["urlDelete"] = reverse_lazy(
            "api_asignacion:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Asignacion.objects.filter(pk=id)

class AsignacionDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = AsignacionForm

    def __init__(self):
        self.service = AsignacionService()
