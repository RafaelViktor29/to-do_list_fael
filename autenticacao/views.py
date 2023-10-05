from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()

        if '' in (username, email, senha):
            messages.add_message(
                request,
                messages.constants.ERROR,
                'Preencha todos os campos'
            )
            return render(request, 'register.html')

        usuario = User.objects.filter(username=username).filter(email=email)

        if usuario.exists():
            messages.add_message(
                request,
                messages.constants.ERROR,
                'E-mail e/ou nome de usuário já cadastrado'
            )
            return redirect('/auth/register')

        try:
            usuario = User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            usuario.save()
            messages.add_message(
                request,
                messages.constants.SUCCESS,
                'Usuário cadastrado com sucesso!'
            )
            return redirect('/auth/login')
        except:
            messages.add_message(
                request,
                messages.constants.ERROR,
                'Erro interno do sistema'
            )
            return redirect('/auth/register')


def login_user(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = authenticate(username=username, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('/tarefas')
        else:
            messages.add_message(
                request,
                messages.constants.ERROR,
                'Nome de usuário e/ou senha inválidos'
            )
            return redirect('/auth/login')


def logout_user(request):
    logout(request)
    return redirect('/auth/login')
