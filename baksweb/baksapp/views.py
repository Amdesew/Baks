from django.shortcuts import render
from .models import HezbeOne, TaxiOne, DerekOne, Automobile, Moter

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def result(request):
    students = ''
    if 'q' in request.GET:
        q = request.GET['q']
        students = HezbeOne.objects.filter(name=q)
        students = TaxiOne.objects.filter(name=q)
        students = DerekOne.objects.filter(name=q)
        students = Automobile.objects.filter(name=q)
        #students = Moter.objects.filter(name=q)
    else:
        print("Failed")
    return render(request, 'result.html', {'students': students})

def youtube(request):
    return render(request, 'youtube.html')

def about(request):
    return render(request, 'about.html')