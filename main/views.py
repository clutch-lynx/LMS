from django.shortcuts import render
from .models import CustomUser
# Create your views here.
def first_page(request):
    return render(request, 'first_page.html')