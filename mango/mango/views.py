from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from products.models import Claim


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

    args = {}
    return render_to_response('settings.html',args)

def in_progress(request):

    saved_claims = Claim.objects.filter(user = request.user, submitted = False) 
    args = {}
    args['saved_claims'] = saved_claims
    return render_to_response('in_progress_page.html',args)


