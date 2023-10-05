from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tarefas/', views.tarefas, name="tarefas"),
    path('add_tarefa/', views.add_tarefa, name="add_tarefa"),
    path('excluir_tarefa/<int:id_tarefa>/',
         views.excluir_tarefa, name="excluir_tarefa"),
    path('editar_tarefa/<int:id_tarefa>/',
         views.editar_tarefa, name="editar_tarefa"),
    path('atualizar_tarefa/', views.atualizar_tarefa, name="atualizar_tarefa"),
]
