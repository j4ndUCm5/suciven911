import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import InfraestructuraService
from ..models import Infraestructura

class InfraestructuraListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/infraestructura.html"

    def get_context_data(self, **kwargs):
        columns = Infraestructura.objects.all()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Infraestructuras"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("infraestructuras:create")
        context["listApiUrl"] = reverse_lazy("api_infraestructuras:list")
        context["updateUrl"] = reverse_lazy("infraestructuras:update", args=[0])
        context["deleteUrl"] = reverse_lazy("infraestructuras:delete", args=[0])
        context["heads"] = columns
        context["columns"] = columns
        return TemplateLayout.init(self, context)

class InfraestructuraListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = InfraestructuraService()
