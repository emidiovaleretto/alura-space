from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants as message_tag
from .forms import SigninForm, SignupForm


def signin(request):
    '''
    View para efetuar o login do usuário.
    Se o método da requisição for POST, o formulário é validado e, se válido,
    o usuário é autenticado e redirecionado para a página inicial.
    Caso contrário, exibe o formulário de login.
    '''
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                messages.add_message(
                    request,
                    message_tag.SUCCESS,
                    'Login efetuado com sucesso!'
                )
                return redirect('index')

            messages.add_message(
                request,
                message_tag.ERROR,
                'Não foi possível efetuar o login. Verifique as suas'
                'credenciais de acesso.'
            )
            return redirect('signin')

    return render(request, 'users/signin.html', {'form': form})


def signup(request):
    '''
    View para cadastrar um novo usuário.
    Se o método da requisição for POST, o formulário é validado e, se válido,
    o usuário é criado e redirecionado para a página de login.
    Caso contrário, exibe o formulário de cadastro.
    '''
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')

            if User.objects.filter(username=name).exists():
                messages.add_message(
                    request,
                    message_tag.ERROR,
                    'Já existe um usuário com esse nome.'
                )
            else:
                user = User.objects.create_user(
                    username=name,
                    email=email,
                    password=password1
                )
                user.save()
                return redirect('signin')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})


def signout(request):
    '''
    View para deslogar o usuário.
    '''
    logout(request)
    messages.add_message(
        request,
        message_tag.SUCCESS,
        'Usuário deslogado com sucesso!'
    )
    return redirect('signin')
