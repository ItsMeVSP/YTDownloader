from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    msg="<h1>Naa Ready thaan Varava</h1>"
    return HttpResponse(msg)
