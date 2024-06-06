from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Flan, ContacForm
from .form import ContacFormForm



def index(request):
        
        flanes = Flan.objects.filter(is_private=False)
        return render(request,'index.html', {'flanes': flanes})
    
def about(request):
        return render(request,'about.html')
    
def welcome(request):
        flanes = Flan.objects.filter(is_private=True)
        
        return render(request, 'welcome.html', {'flanes': flanes})
        #return render(request,'welcome.html')

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