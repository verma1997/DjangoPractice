from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>My Name Is Priyanshu Verma. I am learning Django.")
