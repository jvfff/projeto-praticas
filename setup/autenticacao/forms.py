from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    USER_TYPE_CHOICES = [
        ('ONG', 'ONG'),
        ('Voluntario', 'Voluntário/Funcionário'),
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        required=True,
        label="Você quer se cadastrar como?"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=254, required=True, label="Usuário")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuário ou senha incorretos.")
        return cleaned_data
    
from .models import ONGProfile, VolunteerProfile

class ONGProfileForm(forms.ModelForm):
    class Meta:
        model = ONGProfile
        fields = ['nome_da_ong', 'cnpj', 'endereco', 'telefone', 'email_contato', 
                  'area_atuacao', 'descricao', 'site', 'responsavel_legal', 
                  'documentos', 'logotipo']

        widgets = {
            'nome_da_ong': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email_contato': forms.EmailInput(attrs={'class': 'form-control'}),
            'area_atuacao': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'site': forms.URLInput(attrs={'class': 'form-control'}),
            'responsavel_legal': forms.TextInput(attrs={'class': 'form-control'}),
            'documentos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'logotipo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = [
            'nome_completo',
            'cpf',
            'data_nascimento',
            'genero',
            'endereco',
            'telefone',
            'email_alternativo',
            'profissao',
            'habilidades',
            'disponibilidade',
            'areas_interesse',
            'experiencia_previa',
            'motivacao',
            'referencias',
            'foto_perfil',
        ]
        widgets = {
            'habilidades': forms.Textarea(attrs={'rows': 4}),
            'experiencia_previa': forms.Textarea(attrs={'rows': 4}),
            'motivacao': forms.Textarea(attrs={'rows': 4}),
            'referencias': forms.Textarea(attrs={'rows': 4}),
        }