from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from ..forms import AccionForm
from ..models import Accion
from ..services import AccionService
from templates.sneat import TemplateLayout

class AccionDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Accion"
        context["titleForm"] = "Eliminar accion"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("accion:list")
        context["urlDelete"] = reverse_lazy(
            "api_accion:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Accion.objects.filter(pk=id)


class AccionDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = AccionForm

    def __init__(self):
        self.service = AccionService()
