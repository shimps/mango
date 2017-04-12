from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf

def home(request):

    args = {}
    return render_to_response('home.html',args)

def start_page(request):

    args = {}
    args.update(csrf(request))
    return render_to_response('start_page.html',args)
