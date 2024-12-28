import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import GestionService
from ..models import Gestion

class GestionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/gestion.html"

    def get_context_data(self, **kwargs):
        columns = Gestion.objects.all()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Gestion"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("gestion:create")
        context["listApiUrl"] = reverse_lazy("api_gestion:list")
        context["updateUrl"] = reverse_lazy("gestion:update", args=[0])
        context["deleteUrl"] = reverse_lazy("gestion:delete", args=[0])
        context["heads"] = columns
        context["columns"] = columns
        return TemplateLayout.init(self, context)

class GestionListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = GestionService()
