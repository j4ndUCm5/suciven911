from django.urls import include, path
from .views import PlanificacionView

urlpatterns = [
    path("", PlanificacionView.as_view(),  name="planificacion",),
    path("objetivos/", include(("apps.planificacion.objetivos.urls", "objetivos"))),
    path("api/objetivos/", include(("apps.planificacion.objetivos.urls_apis", "api_objetivos")),),
    path("actividades/", include(("apps.planificacion.actividades.urls", "actividades"))),
    path("api/actividades/", include(("apps.planificacion.actividades.urls_apis", "api_actividades")),),
    path("llamadas/", include(("apps.planificacion.llamadas.urls", "llamadas"))),
    path("api/llamadas/", include(("apps.planificacion.llamadas.urls_apis", "api_llamadas")),),
    path("infraestructuras/",include(("apps.planificacion.infraestructuras.urls", "infraestructuras")),),
    path("api/infraestructuras/", include(("apps.planificacion.infraestructuras.urls_apis", "api_infraestructuras") ),),
    path("transportes/",  include(("apps.planificacion.transportes.urls", "transportes")),),
    path( "api/transportes/", include(("apps.planificacion.transportes.urls_apis", "api_transportes")), ),
]
