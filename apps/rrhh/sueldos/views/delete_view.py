from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import SueldoForm
from ..models import Sueldo
from ..services import SueldoService


class SueldoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Sueldos"
        context["titleForm"] = "Eliminar sueldo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("sueldos:list")
        context["urlDelete"] = reverse_lazy(
            "api_sueldos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Sueldo.objects.filter(pk=id)


class SueldoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = SueldoForm

    def __init__(self):
        self.service = SueldoService()
