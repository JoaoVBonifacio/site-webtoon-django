# webtoons/views.py
from django.shortcuts import render, get_object_or_404
from .models import Webtoon, Capitulo
from django.db.models import Prefetch
from django.shortcuts import redirect # Adicione redirect
from django.contrib.auth.decorators import login_required # Para proteger a página
from .forms import WebtoonForm # Importe nosso novo formulário
from django.contrib.auth import logout # Adicione este

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

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required # Garante que apenas usuários logados possam acessar esta página
def criar_webtoon(request):
    if not request.user.is_superuser:
        # Opcional: Redireciona se o usuário não for um admin
        return redirect('home')

    if request.method == 'POST':
        # Se o formulário foi enviado, processa os dados
        form = WebtoonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Salva a nova webtoon no banco de dados
            return redirect('home') # Redireciona para a página inicial após o sucesso
    else:
        # Se for o primeiro acesso (GET), mostra um formulário em branco
        form = WebtoonForm()

    return render(request, 'webtoon_form.html', {'form': form})