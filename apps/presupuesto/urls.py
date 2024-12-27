from django.urls import include, path
from .views import PresupuestoView

urlpatterns = [
    path("", PresupuestoView.as_view(), name="presupuesto",),
    path("proyecto/", include(("apps.presupuesto.proyecto.urls", "proyecto"))),
    path("api/proyecto/",include(("apps.presupuesto.proyecto.urls_apis", "api_proyecto")),),
    path("acciones/", include(("apps.presupuesto.acciones.urls", "acciones"))),
    path("api/acciones/",include(("apps.presupuesto.acciones.urls_apis", "api_acciones")),),
    path("asignacion/", include(("apps.presupuesto.asignacion.urls", "asignacion"))),
    path("api/asignacion/",include(("apps.presupuesto.asignacion.urls_apis", "api_asignacion")),),
    path("cedente/", include(("apps.presupuesto.cedente.urls", "cedente"))),
    path("api/cedente/",include(("apps.presupuesto.cedente.urls_apis", "api_cedente")),),
    path("receptor/", include(("apps.presupuesto.receptor.urls", "receptor"))),
    path("api/receptor/",include(("apps.presupuesto.receptor.urls_apis", "api_receptor")),),
]