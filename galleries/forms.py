from django import forms


class PhotoForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Ex.: Aurora Boreal'
            }
        )
    )
    caption = forms.CharField(
        label='Legenda',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Ex.: Aurora Boreal em Tromso, Noruega'
            }
        )
    )
    description = forms.CharField(
        label='Descrição',
        widget=forms.Textarea(
            attrs={
                'class': 'input-text',
                'placeholder':
                'Ex.: A aurora boreal é um fenômeno natural que ocorre em regiões polares.'
            }
        )
    )
    category = forms.ChoiceField(
        label='Categoria',
        choices=(
            ('NEBULOSA', 'Nebulosa'),
            ('GALAXIA', 'Galaxia'),
            ('PLANETA', 'Planeta'),
            ('ESTRELLA', 'Estrela'),
        ),
        widget=forms.Select(
            attrs={
                'class': 'input-text',
                'placeholder': 'Select a category'
            }
        )
    )
    image = forms.ImageField(
        label='Imagem',
        widget=forms.FileInput(
            attrs={
                'class': 'input-text',
                'placeholder': 'Select an image'
            }
        )
    )
