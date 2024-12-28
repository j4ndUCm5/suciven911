import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import CedenteService
from ..models import Cedente

class CedenteListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/cedente.html"

    def get_context_data(self, **kwargs):
        columns = Cedente.objects.all()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Cedente"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("cedente:create")
        context["listApiUrl"] = reverse_lazy("api_cedente:list")
        context["updateUrl"] = reverse_lazy("cedente:update", args=[0])
        context["deleteUrl"] = reverse_lazy("cedente:delete", args=[0])
        context["exportPdfUrl"] = reverse_lazy("api_cedente:export_pdf")
        context["heads"] = columns
        context["columns"] = columns
        return TemplateLayout.init(self, context)

class CedenteListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = CedenteService()
