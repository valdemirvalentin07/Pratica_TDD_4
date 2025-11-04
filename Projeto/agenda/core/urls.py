from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('contatos/', views.lista_contatos, name='listar_contatos'),
    path('contatos/novo/', views.novo_contato, name='novo_contato'),
    path('contatos/editar/<int:id>/', views.editar_contato, name='editar_contato'),
    path('contatos/excluir/<int:id>/', views.excluir_contato, name='excluir_contato'),
    path('contatos/editar/', views.lista_edita, name='lista_edita'),
    path('contatos/lista_exclui/', views.lista_exclui, name='lista_exclui'),

]







