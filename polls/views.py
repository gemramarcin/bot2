from django.http import HttpResponse
from django.shortcuts import render
import requests
import sys
from subprocess import run, PIPE


def homePage(request):
    return render(request, 'home.html')

# def output(request):

#     data=requests.get("https://reqres.in/api/users")
#     print(data.text)
#     data=data.text
#     return render(request, 'home.html', {'data':data})

def external(request):
    out=run([sys.executable,'C:\\Users\\mgemra\\GettinJobProjects\\mysite\\polls\\main.py'], shell=False, stdout = PIPE)
    return render(request, 'home.html', {'data':out})

def index(request):
    return render(request, 'index.html')

    
def packetGen(request):
    return render(request, 'packetGen.html')

    
def help(request):
    return render(request, 'help.html')

    
def scenario(request):
    return render(request, 'scenario.html')