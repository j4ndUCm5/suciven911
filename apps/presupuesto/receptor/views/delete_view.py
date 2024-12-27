from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from templates.sneat import TemplateLayout
from ..forms import ReceptorForm
from ..models import Receptor
from ..services import ReceptorService

class ReceptorDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Receptor"
        context["titleForm"] = "Eliminar receptor"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("receptor:list")
        context["urlDelete"] = reverse_lazy("api_receptor:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Receptor.objects.filter(pk=id)

class ReceptorDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = ReceptorForm

    def __init__(self):
        self.service = ReceptorService()
