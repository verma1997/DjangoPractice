from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'templates/base.html')

def other(request):
    return render(request, 'templates/other.html')

def index(request):
    return render(request, 'templates/index.html')
