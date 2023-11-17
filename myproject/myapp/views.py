# myapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def other_page(request):
    return render(request, 'other_page.html')
