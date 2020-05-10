from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
import requests
import sys
from subprocess import run, PIPE
from PythonScripts import main
from polls import forms



def homePage(request):
    return render(request, 'home.html')

# def output(request):

#     data=requests.get("https://reqres.in/api/users")
#     print(data.text)
#     data=data.text
#     return render(request, 'home.html', {'data':data})

def external(request):
    #ut=run([sys.executable,'C:\\Users\\Pawel\\Desktop\\BOT-Project\\PythonScripts\\main.py'], shell=False, stdout = PIPE)
    out = main.choose(3)
    return render(request, 'home.html', {'data':out})

def index(request):
    return render(request, 'index.html')

    
def packetGen(request):
    return render(request, 'packetGen.html')

    
def help(request):
    return render(request, 'help.html')

    
def scenario(request):
        # if this is a POST request we need to process the form data

    out = "result:"
    if request.method == 'POST':
        inp_value = request.POST.get('scen', 'This is a default value')
        print(inp_value)
        out = main.choose(inp_value)
        
     

    return render(request, 'scenario.html', {'data':out})
    #return render(request, 'scenario.html')