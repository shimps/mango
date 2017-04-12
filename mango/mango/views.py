from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse


def home(request):

    args = {}
    return render_to_response('home.html',args)

def start_page(request):

    args = {}
    return render_to_response('start_page.html',args)
