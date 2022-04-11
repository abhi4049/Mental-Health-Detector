from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
    
def analyze(request):
    return render(request, 'analyze.html')
    
def aboutus(request):
    return render(request, 'aboutus.html')
    
def partner(request):
    return render(request, 'partner.html')
def results(request):
    return HttpResponse('''Results''')
