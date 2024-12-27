from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from weasyprint import HTML
from PyPDF2 import PdfReader
from django.template.loader import render_to_string
from django.shortcuts import HttpResponse
from ..models import Proyecto

class ProyectoPDFView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    def get(self, request, *args, **kwargs):
        accioness = Proyecto.objects.all()
        html_string_with_index = render_to_string('sneat/layout/partials/proyectopdf.html', {
            'Proyectoo': accioness,
        })
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte.pdf"'
        HTML(string=html_string_with_index, base_url=request.build_absolute_uri('/')).write_pdf(response)
        return response