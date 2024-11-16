from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SigninForm, SignupForm


def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(
                request,
                'Login efetuado com sucesso!'
            )
            return redirect('index')
        else:
            messages.error(
                request,
                'Não foi possível efetuar o login. Verifique as suas credenciais de acesso.'
            )
            return redirect('signin')

    return render(request, 'users/signin.html', {'form': form})


def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(
                request,
                'As senhas não conferem.'
            )
            return redirect('index')

        if User.objects.filter(username=name).exists():
            messages.error(
                request,
                'Já existe um usuário com esse nome.'
            )
            return redirect('signup')

        user = User.objects.create_user(
            username=name, 
            email=email, 
            password=password1
        )
        user.save()
        messages.success(
            request,
            'Usuário cadastrado com sucesso!'
        )
        return redirect('signin')

    return render(request, 'users/signup.html', {'form': form})


def signout(request):
    logout(request)
    messages.success(
        request,
        'Usuário deslogado com sucesso!'
    )
    return redirect('signin')
    