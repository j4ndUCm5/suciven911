import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import TransporteService
from ..models import Transporte

class TransporteListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/transportes.html"

    def get_context_data(self, **kwargs):
        columns = Transporte.objects.all()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Transportes"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("transportes:create")
        context["listApiUrl"] = reverse_lazy("api_transportes:list")
        context["updateUrl"] = reverse_lazy("transportes:update", args=[0])
        context["deleteUrl"] = reverse_lazy("transportes:delete", args=[0])
        context["heads"] = columns
        context["columns"] = columns
        return TemplateLayout.init(self, context)

class TransporteListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = TransporteService()
