# from ckeditor_uploader import forms
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.db.models import Count
from django.contrib.auth import login, authenticate, logout
from .forms import LoginFrom, RegisterDataFrom, RegisterDataSemanticFrom
# from django.contrib import auth
from .models import *
from django.core import serializers
from django.http import HttpResponse
import rdflib


# Create your views here.
def home(request):
    return render(request, "home.html")


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            usernm = request.POST['username']
            passwrd = request.POST['password']
            user = authenticate(request, username=usernm, password=passwrd)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
            else:
                form = LoginFrom()
                args = {'form': form}
                return render(request, 'ttapp/login.html', args)
        else:
            form = LoginFrom()
            args = {'form': form}
            return render(request, 'ttapp/login.html', args)
    else:
        return redirect('/admin/')


def logout_view(request):
    logout(request)
    return redirect('/')


def registerData(request):
    if request.method == 'POST':
        form = RegisterDataFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("saveeeeeee")
            print(form)
        return redirect("/")
    else:
        form = RegisterDataFrom()
    return render(request, 'ttapp/register.html', {'form': form})


def registerDataSemantic(request):
    if request.method == 'POST':
        form = RegisterDataSemanticFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("saveeeeeee")
            print(form)
        return redirect("/")
    else:
        form = RegisterDataSemanticFrom()
    return render(request, 'ttapp/registerNew.html', {'form': form})


def api(request):
    list_API = serializers.serialize('json', repositoryNew.objects.all())
    data = {}
    data['status'] = '200 ok'
    return HttpResponse(list_API, content_type='application/json')


def apiDataSemantic(request):
    list_API = serializers.serialize('json', DataTurtel.objects.all())
    data = {}
    data['status'] = '200 ok'
    return HttpResponse(list_API, content_type='application/json')


def ner_entity(request):
    return render(request, "spacy-ner-annotator/NERSpacy.html")


g = rdflib.Graph()
# result = g.parse('trees.ttl')
# result = g.parse('portal/data/tripletasCkan_EhWSmkp.ttl', format='ttl')
# result = g.parse('trees.ttl', format='n3')
print(len(g))
for stmt in g:
    print(stmt)