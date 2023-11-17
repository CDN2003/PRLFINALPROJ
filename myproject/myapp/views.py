# myapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def target_page(request):
    return render(request, 'target_page.html')
