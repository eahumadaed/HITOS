from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Flan, ContacForm,CategoriasProducto
from .form import ContacFormForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.views import View
from django.urls import reverse
from django.contrib import messages

def index(request):
        categorias_flanes = CategoriasProducto.objects.get(name='Flan')
        flanes = Flan.objects.filter(is_private=False,category=categorias_flanes)
        return render(request,'index.html', {'flanes': flanes})

def custom_logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect(reverse('index'))
    
def about(request):
        return render(request,'about.html')
    
def welcome(request):
        categorias_flanes = CategoriasProducto.objects.get(name='Flan')
        flanes = Flan.objects.filter(is_private=True,category=categorias_flanes)
        return render(request, 'welcome.html', {'flanes': flanes})

def productos(request):
        categorias = CategoriasProducto.objects.get(name='Flan')
        productos = Flan.objects.exclude(category=categorias)
        return render(request, 'productos.html', {'productos': productos})


def contacto(request):
        if request.method == 'POST':
                form = ContacFormForm(request.POST)
                if form.is_valid():
                        contact_form = ContacForm.objects.create(**form.cleaned_data)
                        return HttpResponseRedirect('/exito')
        else:
                form = ContacFormForm()
        return render(request,'contacto.html',{'form':form})

def exito(request):
        return render(request,'exito.html')

class RegisterView(View):
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index') 
        return render(request, 'registration/register.html', {'form': form})