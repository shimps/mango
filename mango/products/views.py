from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from models import Policy
from accounts.models import InsuranceCompanyAccount
from products.models import Policy, insurance_category_choices

# Create your views here.
def insurance_types(request):

    args = {}
    return render_to_response('insurance_types.html',args)

def create_policy(request):

    if request.POST:
        
        title = request.POST['title']
        category = request.POST['category']
        max_cover = request.POST['max_cover']
        coinsurance = request.POST['coinsurance']
        deductible = request.POST['deductible']
        monthly_cost = request.POST['monthly_cost']
        logged_user = request.user
        try:
            insurance_company = logged_user.insurance_company_profile
            Policy.objects.create(title = title, category = category, max_cover = max_cover,
                              coinsurance = coinsurance, deductible = deductible, monthly_cost = monthly_cost,
                              insurance_company = insurance_company)
        
            return HttpResponseRedirect('/')
        except:
            return HttpResponse('Something went wrong :(')

    args = {}
    args.update(csrf(request))
    return render_to_response('create_policy_page.html',args)

def view_policy(request):

    policy_id = request.GET.get('policy_id')
    policy = Policy.objects.get(id = policy_id)
    
    args = {}
    args['policy'] = policy
    return render_to_response('policy_page.html',args)

def view_claims(request):
    args = {}
    return render_to_response('claims.html',args)

def get_category_string(category_letter):
    for category in insurance_category_choices:
        if category[0] == category_letter:
            return category[1]
    return None

def my_insurance(request):

    args = {}
    return render_to_response('my_insurance.html',args)

def view_policies(request):

    try:
        policy_category = request.GET.get('category')
        category = get_category_string(policy_category)
    except:
        return HttpResponse('Something went wrong :(')
    
    policies = Policy.objects.filter(category = policy_category)
    
    args = {}
    args['policies'] = policies
    args['category'] = category
    return render_to_response('policy_list.html',args)
