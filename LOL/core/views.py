from django.shortcuts import render

# Create your views here.

#uma view Django é uma função Python 
def index(resquest):
    return render(request, 'index.html')

def index(resquest):
    return render(request, 'contato.html')