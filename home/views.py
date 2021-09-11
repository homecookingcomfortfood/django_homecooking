from django.shortcuts import render, HttpResponse
from home import models
from datetime import datetime
from home.models import Contact, smoothie, receipe, frontimage
from django.contrib import messages
from django.views.generic import ListView, DetailView
  

# Create your views here.

def index(request):
    recp = frontimage.objects.all()
    return render(request,'index.html',{'frontimage': recp })

def home(request):
    recp = frontimage.objects.all()
    return render(request,'index.html',{'frontimage': recp })

def about(request):
    return render(request,'about.html')

def receipes(request):
    return render(request,'products.html')

class HomeView(ListView):
    model = receipe
    template_name = 'Receipelist.html'

class ReceipeDetailView(DetailView):
    model = receipe
    template_name = 'ReceipeDtlist.html'

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
      
        contact = Contact(name=name, email = email, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been submitted !!')
    return render(request,'contact.html')

def smoothies(request):
    smth = smoothie.objects.all()
    return render(request,'smoothies.html',{'smoothie': smth })

def maindishes(request):
    return render(request,'maindishes.html')

def tacor(request):
    return render(request,'tacor.html')

def apricotr(request):
    return render(request,'apricotr.html')

def padr(request):
    return render(request,'padr.html')

def methir(request):
    return render(request,'methir.html')

def brownr(request):
    return render(request,'brownr.html')

def falr(request):
    return render(request,'falr.html')

def sandw(request):
    return render(request,'sandw.html')

def cutlets(request):
    return render(request,'cutlets.html')

def pestop(request):
    return render(request,'pestop.html')

def calzone(request):
    return render(request,'calzone.html')