from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author

def index(request):
    return HttpResponse("Anasayfa")
def authors(request):
    template = loader.get_template('authors.html')

    context = {
        'author_list' : Author.objects.all()
    } 
    return HttpResponse(template.render(context,request))

def books(request):
    return HttpResponse("Kitaplar")
def authorsDetails(request,authorId):
    return HttpResponse("Yazar Detayı "+ str(authorId))