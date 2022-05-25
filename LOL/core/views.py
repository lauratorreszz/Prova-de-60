from django.shortcuts import render

# Create your views here.

#uma view Django é uma função Python 
def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')