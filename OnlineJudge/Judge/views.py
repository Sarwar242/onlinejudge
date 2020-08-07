from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><strong>Welcome To Online Judge</strong> <br> It is now %s.</body></html>" % now
    return HttpResponse(html)