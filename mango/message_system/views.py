from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def view_messages(request):

    args = {}
    return render_to_response('messages.html',args)
