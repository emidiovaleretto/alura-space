from django import forms


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
        label="Nome completo", 
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Ex.: João Silva'
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
