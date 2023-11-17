# myapp/urls.py
from django.urls import path    
from .views import index, other_page

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('other/', other_page, name='other_page'),  # Add this line for the new page
]
