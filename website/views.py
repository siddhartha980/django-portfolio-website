from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'website/home.html')

def blog(request):
    return render(request,'website/blog.html')

def portfolio(request):
    return render(request,'website/portfolio.html')

def contact(request):
    return render(request,'website/contact.html')

def contactus(request):
    return render(request,'website/contactus.html')

def mycv(request):
    return render(request,'website/mycv.html')
    
def research(request):
    return render(request,'website/research.html')