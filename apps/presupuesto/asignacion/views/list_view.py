import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import AsignacionService
from ..models import Asignacion

class AsignacionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/asignacion.html"

    def get_context_data(self, **kwargs):
        columns = Asignacion.objects.all()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Asignacion"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("asignacion:create")
        context["listApiUrl"] = reverse_lazy("api_asignacion:list")
        context["updateUrl"] = reverse_lazy("asignacion:update", args=[0])
        context["deleteUrl"] = reverse_lazy("asignacion:delete", args=[0])
        context["exportPdfUrl"] = reverse_lazy("api_asignacion:export_pdf")
        context["heads"] = columns
        context["columns"] = columns
        return TemplateLayout.init(self, context)

class AsignacionListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = AsignacionService()
