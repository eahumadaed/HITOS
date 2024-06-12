from django import forms
from django.contrib.auth.models import User


#Manejo de formulario de contacto.
class ContacFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')
    
    
#formulario de registro de usuario
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  #Campos que se solicitaran

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        #En caso que la contraseña no coincida, no pasara la validacion.             
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data