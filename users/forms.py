from django import forms
from django.core.exceptions import ValidationError


class SigninForm(forms.Form):
    username = forms.CharField(
        label="Nome de Login",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Digite o seu nome de login',
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Digite sua senha'
            }
        )
    )


class SignupForm(forms.Form):
    name = forms.CharField(
        label="Usuário",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Ex.: JoãoSilva'
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Ex.: joaosilva@xpto.com'
            }
        )
    )
    password1 = forms.CharField(
        label="Senha",
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirmação de senha",
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )

    def clean_name(self):
        data = self.cleaned_data.get("name")

        if data:
            data = data.strip()

            if ' ' in data:
                raise ValidationError(
                    'Não é possível inserir espaços dentro do campo (usuário)'
                )

            return data

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    'As senhas não conferem.'
                )

            return password2
