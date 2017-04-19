from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from accounts.models import ClientAccount, CompanyAccount
from products.models import Claim, ClientPolicy, CompanyPolicy,Application


@login_required
def home(request):

    logged_user = request.user
    
    args = {}
    
    my_policies = []
    
    if logged_user.account_type.individual == True:
        client_account = ClientAccount.objects.get(user = request.user)
        my_policies = ClientPolicy.objects.filter(client = client_account,cancelled = False)

    elif logged_user.account_type.company == True:
        company_account = CompanyAccount.objects.get(user = request.user)
        my_policies = CompanyPolicy.objects.filter(company = company_account)
        
    args['current_policies'] = my_policies
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
    saved_applications = Application.objects.filter(user = request.user, submitted = False)
    args = {}
    args['saved_claims'] = saved_claims
    args['application_forms'] = saved_applications
    return render_to_response('in_progress_page.html',args)


