from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me':"See! I am the content which is inserted from views.py.!"}
    return render(request,'first/index.html',context=my_dict)
