from django.shortcuts import render
#from django.http import HttpResponse
from ProjectApp.models import User
# Create your views here.

#def index(request):
#    my_dict = {'insert_me':"See! I am the content which is inserted from views.py.!"}
#    return render(request,'first/index.html',context=my_dict)

def index(request):
    return render(request,'first/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'first/users.html',context=user_dict)
