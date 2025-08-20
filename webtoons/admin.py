# webtoons/admin.py

from django.contrib import admin
from .models import Webtoon, Capitulo, Pagina

# Esta é a forma padrão do Django, que vamos aprimorar.
class PaginaInline(admin.TabularInline):
    model = Pagina
    extra = 1 # Começamos com 1 linha em branco para adicionar a primeira página
    ordering = ('ordem',)


@admin.register(Capitulo)
class CapituloAdmin(admin.ModelAdmin):
    inlines = [PaginaInline]
    list_display = ('__str__', 'webtoon', 'numero')
    list_filter = ('webtoon',)

    # AQUI ESTÁ A LÓGICA DA AUTO-NUMERAÇÃO
    def save_formset(self, request, form, formset, change):
        # Primeiro, deixamos o Django salvar tudo normalmente
        super().save_formset(request, form, formset, change)

        # 'formset.instance' é o objeto Capítulo que estamos salvando
        capitulo = formset.instance
        
        # Pegamos todas as páginas recém-salvas que ainda não têm uma ordem definida
        paginas_sem_ordem = capitulo.paginas.filter(ordem__isnull=True)

        # Verificamos qual é a maior ordem já existente para este capítulo
        try:
            maior_ordem = capitulo.paginas.exclude(ordem__isnull=True).latest('ordem').ordem
        except Pagina.DoesNotExist:
            maior_ordem = 0

        # Agora, para cada página nova, atribuímos a ordem correta
        for i, pagina in enumerate(paginas_sem_ordem):
            pagina.ordem = maior_ordem + i + 1
            pagina.save()


@admin.register(Webtoon)
class WebtoonAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'status')
    search_fields = ('titulo', 'autor')