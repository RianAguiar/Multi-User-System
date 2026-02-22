from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DocumentoForm

# Create your views here.
def homepage1(request):
    return render(request,'user1/HomePage1.html')

def homepage2(request):
    return render(request,'user2/HomePage2.html')