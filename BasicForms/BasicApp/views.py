from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicApp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING LANGUAGE_CODE
            print("Validation Success !")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Password: "+form.cleaned_data['password'])
            print("Text: "+form.cleaned_data['text'])

    return render(request,'basicApp/form_page.html',{'form':form})
