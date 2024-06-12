from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Flan, ContacForm,CategoriasProducto
from .form import ContacFormForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.views import View
from django.urls import reverse
from django.contrib import messages


#Vista del index, el cual solo muestra los productos que son Flan y que no son privados
def index(request):
        categorias_flanes = CategoriasProducto.objects.get(name='Flan') #Obtiene la id de la categoria Flan en la tabla CategoriasProducto
        flanes = Flan.objects.filter(is_private=False,category=categorias_flanes) #Filtra los productos por la ID y el campo is_private
        
        return render(request,'index.html', {'flanes': flanes})



#vista apartado ABOUT
def about(request):
        return render(request,'about.html')

#Vista del welcome, el cual solo muestra productos que son Flan y privados
def welcome(request):
        categorias_flanes = CategoriasProducto.objects.get(name='Flan')  #Obtiene la id de la categoria Flan en la tabla CategoriasProducto
        flanes = Flan.objects.filter(is_private=True,category=categorias_flanes) #Filtra los productos por la ID y el campo is_private
        return render(request, 'welcome.html', {'flanes': flanes})

#Vista personalidad de productos, el cual muestra productos que no son Flan
def productos(request):
        categorias = CategoriasProducto.objects.get(name='Flan') #Obtiene la id de la categoria Flan en la tabla CategoriasProducto
        productos = Flan.objects.exclude(category=categorias) #Se excluye la categoria de productos usando la ID
        return render(request, 'productos.html', {'productos': productos})


#Vista del formulario de contacto
def contacto(request):
        if request.method == 'POST':  #En caso que detecte un POST se guarda
                form = ContacFormForm(request.POST)
                if form.is_valid():  #Valida el formulario
                        contact_form = ContacForm.objects.create(**form.cleaned_data)
                        return HttpResponseRedirect('/exito')  #Redirigue a la vista exito.
        else:
                form = ContacFormForm()
        return render(request,'contacto.html',{'form':form})

#Vista del Apartado Exito
def exito(request):
        return render(request,'exito.html')

#Vista personalidad del logout, el cual muestra un mensaje de cierre de sesión
def custom_logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect(reverse('index'))


#Vista del formulario de registro.
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