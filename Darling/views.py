from django.shortcuts import render

# Create your views here.

def basic(request):
    return render(request,'sk/basic.html')
def navbar(request):
    return render(request,'sk/navbar.html')
def register(request):
	return render(request,'sk/register.html')