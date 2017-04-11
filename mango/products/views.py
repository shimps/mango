from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def insurance_types(request):

    args = {}
    return render_to_response('insurance_types.html',args)
