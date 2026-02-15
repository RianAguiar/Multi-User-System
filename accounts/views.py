from django.shortcuts import render

# Create your views here.
def homepage1(request):
    return render(request,'user1/HomePage1.html')

def homepage2(request):
    return render(request,'user2/HomePage2.html')