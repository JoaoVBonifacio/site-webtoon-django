# webtoons/views.py
from django.shortcuts import render, get_object_or_404
from .models import Webtoon, Capitulo
from django.db.models import Prefetch

def home(request):
    # Usamos Prefetch para buscar os capítulos de forma otimizada
    webtoons = Webtoon.objects.prefetch_related('capitulos').all()
    context = {'lista_webtoons': webtoons}
    return render(request, 'home.html', context)

def leitor_capitulo(request, capitulo_id):
    # Busca o capítulo pelo ID ou retorna um erro 404 (página não encontrada)
    capitulo = get_object_or_404(Capitulo.objects.prefetch_related('paginas'), id=capitulo_id)
    context = {'capitulo': capitulo}
    return render(request, 'leitor.html', context)

def detalhes_webtoon(request, webtoon_id):
    webtoon = get_object_or_404(Webtoon.objects.prefetch_related('capitulos'), id=webtoon_id)
    context = {'webtoon': webtoon}
    return render(request, 'detalhes.html', context)