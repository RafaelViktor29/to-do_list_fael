from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Tarefa


def home(request):
    return redirect('/auth/login')


@login_required
def tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'tarefas.html', context={'tarefas': tarefas})


@login_required
def add_tarefa(request):
    titulo = request.POST.get('tarefa').strip()

    if len(titulo) > 54:
        messages.add_message(
            request,
            messages.constants.ERROR,
            'A tarefa deve ter no máximo 54 caracteres'
        )
        return redirect('/tarefas')

    if len(titulo) > 0:
        nova_tarefa = Tarefa(titulo=titulo, usuario=request.user)
        nova_tarefa.save()

    return redirect('/tarefas')


@login_required
def excluir_tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)
    tarefa.delete()
    return redirect('/tarefas')


@login_required
def editar_tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)

    if request.method == "GET":
        return render(request, 'editar_tarefa.html', context={
            'tarefa': tarefa
        })
    elif request.method == "POST":
        titulo = request.POST.get('tarefa')

        if len(titulo) > 54:
            messages.add_message(
                request,
                messages.constants.ERROR,
                'A tarefa deve ter no máximo 54 caracteres'
            )
            return redirect('/tarefas')

        if len(titulo) > 0:
            tarefa.titulo = titulo
            tarefa.save()

        return redirect('/tarefas')


@csrf_exempt
def atualizar_tarefa(request):
    if request.method == "POST":
        tarefa_id = request.POST.get('tarefa_id')
        status = request.POST.get('status')
        try:
            tarefa = Tarefa.objects.get(id=tarefa_id)
            tarefa.status = status
            tarefa.save()
            return JsonResponse({
                "mensagem": "Status da tarefa atualizado com sucesso."})
        except Tarefa.DoesNotExist:
            return JsonResponse({"erro": "A tarefa não existe."})
    else:
        return JsonResponse({"erro": "Método inválido."})
