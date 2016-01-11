from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from models import Test, TestSaveToDatabase
# Create your views here.

def index(request):
    template = loader.get_template('main/index.html')
    TestSaveToDatabase()
    context = {

    }
    return HttpResponse(template.render(context, request))
