from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

def registration(request):

    account_type = request.GET.get('account_type')
    args = {}
    args.update(csrf(request))

    if account_type == 'I':
        return render_to_response('individual_registration_page.html',args)
    
    elif account_type == 'C':
        return render_to_response('company_registration_page.html',args)
    
    elif account_type == 'M':
        return render_to_response('medical_registration_page.html',args)
    
    elif account_type == 'P':
        return render_to_response('police_registration_page.html',args)
    
    elif account_type == 'S':
        return render_to_response('service_agent_registration_page.html',args)

    
    return HttpResponse('Something went wrong :(')

def create_individual_account(request):
    
    return HttpResponse('Individual Registration')

def create_company_account(request):
    
    return HttpResponse('Company Registration')

def create_medical_account(request):
    
    return HttpResponse('Medical Institution Registration')

def create_police_account(request):
    
    return HttpResponse('Police Account Registration')

def create_service_agent_account(request):
    
    return HttpResponse('Service Agent Registration')
