from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Ocorrencia
from .forms import OcorrenciaForm

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class CriarOcorrenciaView(View):
    def get(self, request):
        form = OcorrenciaForm()
        return render(request, 'criar_ocorrencia.html', {'form': form})

    def post(self, request):
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Denúncia enviada com sucesso.')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao enviar denúncia. Verifique os campos.')
        return render(request, 'criar_ocorrencia.html', {'form': form})

class ListaOcorrenciasView(View):
    def get(self, request):
        ocorrencias = Ocorrencia.objects.all().order_by('-data')
        return render(request, 'lista_ocorrencias.html', {'ocorrencias': ocorrencias})
