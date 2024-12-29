from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from templates.sneat import TemplateLayout
from ..forms import GestionForm
from ..models import Gestion
from ..services import GestionService

class GestionUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = GestionForm
    template_name = "sneat/layout/partials/form/layout_gestion_editar.html"

    def get_context_data(self, **kwargs):
        id = self.kwargs.get("pk")
        data = Gestion.objects.filter(pk=id).all
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Gestion"
        context["titleForm"] = "Actualizar gestion"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("gestion:list")
        context["urlForm"] = reverse_lazy("api_gestion:update", args=[self.kwargs.get("pk")])
        context["methodForm"] = "PUT"
        context["formu"] = data
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Gestion.objects.filter(pk=id)

class GestionUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = GestionForm

    def __init__(self):
        self.service = GestionService()
