from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    '''
    Formulário para adicionar uma nova imagem
    '''
    name = forms.CharField(max_length=100, required=True)
    caption = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea())
    category = forms.ChoiceField(choices=Photo.CATEGORY_CHOICES, required=True)
    image = forms.ImageField()

    class Meta:
        '''
        Meta informações do formulário
        '''
        model = Photo
        fields = ['name', 'caption', 'description', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Ex.: Aurora Boreal',
            'caption': 'Ex.: Aurora Boreal em Tromso, Noruega',
            'description':
            'Ex.: A aurora boreal é um fenômeno natural que ocorre em regiões polares.',
            'category': 'Selecione uma categoria',
            'image': 'Selecione uma imagem'
        }

        print(self.fields)

        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'category':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            else:
                self.fields[field].label = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'input-text'
