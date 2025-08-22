# webtoons/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # URL para os detalhes da webtoon: ex: /webtoon/1/
    path('webtoon/<int:webtoon_id>/', views.detalhes_webtoon, name='detalhes_webtoon'),
    # URL para o leitor de capítulo: ex: /capitulo/5/
    path('capitulo/<int:capitulo_id>/', views.leitor_capitulo, name='leitor'),
    # ADICIONE A NOVA URL AQUI
    path('webtoon/adicionar/', views.criar_webtoon, name='webtoon_form'),
    path('sair/', views.logout_view, name='logout'),
]