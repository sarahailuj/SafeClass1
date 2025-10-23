from django.contrib import admin
from django.urls import path
from app.views import IndexView, CriarOcorrenciaView, ListaOcorrenciasView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('denunciar/', CriarOcorrenciaView.as_view(), name='criar_ocorrencia'),
    path('ocorrencias/', ListaOcorrenciasView.as_view(), name='lista_ocorrencias'),
]
