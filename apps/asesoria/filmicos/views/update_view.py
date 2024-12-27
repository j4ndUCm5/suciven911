from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import RegistroFilmicoForm
from ..models import RegistroFilmico
from ..services import RegistroFilmicoService


class RegistroFilmicoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = RegistroFilmicoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Registro Filmico"
        context["titleForm"] = "Actualizar Registro Filmico"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("filmicos:list")
        context["urlForm"] = reverse_lazy(
            "api_filmicos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return RegistroFilmico.objects.filter(pk=id)


class RegistroFilmicoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = RegistroFilmicoForm

    def __init__(self):
        self.service = RegistroFilmicoService()
