from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required


@login_required
def home(request):

    logged_user = request.user
    args = {}
    args['logged_user'] = logged_user
    return render_to_response('home.html',args)

def start_page(request):

    args = {}
    args.update(csrf(request))
    return render_to_response('start_page.html',args)

def settings(request):

    return HttpResponse('settings')

def in_progress(request):

    return HttpResponse('in progress')
