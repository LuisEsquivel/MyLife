from django import forms
from First.QWEQWEQWEQ.NoSeQuePedo.models import AñadirUsuarios



class NewUser(forms.ModelForm):
    class Meta:
        model = AñadirUsuarios

        fields = [
            'Nombrazo',
            'Apellidos',
            'Email',
            'Contraseña',
        ]

        labels = {
            'Nombrazo': 'Nombre',
            'Apellidos': 'Apellido(s)',
            'Email':'Correo electronico',
            'Contraseña':'Contraseña',
    }

        widgets = {
            'Nombrazo': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'Contraseña': forms.TextInput(attrs={'class': 'form-control'}),
        }

