from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formularioProfesor(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class formularioEstudiante(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    fechaCumple = forms.DateField()
    email= forms.EmailField()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label = 'Repite la Contraseña', widget= forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label='Pass', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita Pass', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

