from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import ClientAccount, CompanyAccount, InsuranceCompanyAccount, PoliceAgentAccount, MedicalAgentAccount, InsuranceCompanyAccount, MangoAgent, AccountType

# Create your views here.

def registration(request):

    account_type = request.GET.get('account_type')
    args = {}
    args.update(csrf(request))
    args['account_type'] = account_type
    
    if account_type == 'I':
        return render_to_response('individual_registration_page.html',args)
    
    elif account_type == 'C':
        return render_to_response('company_registration_page.html',args)

    elif account_type == 'IP':
        return render_to_response('insurance_provider_registration_page.html',args)
    
    elif account_type == 'M':
        return render_to_response('medical_registration_page.html',args)
    
    elif account_type == 'P':
        return render_to_response('police_registration_page.html',args)
    
    elif account_type == 'S':
        return render_to_response('service_agent_registration_page.html',args)

    
    return HttpResponse('Something went wrong :(')

def login(request):

    username = request.POST['username']
    password = request.POST['password']

    authenticated_user = auth.authenticate(username = username, password = password)

    if authenticated_user is not None:
        auth.login(request, authenticated_user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('login failed')

def logout(request):

    auth.logout(request)
    return HttpResponseRedirect('/')

def create_individual_account(request):

    if request.POST:
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        title = request.POST['title']
        day_of_birth = request.POST['birth_day']
        month_of_birth = request.POST['birth_month']
        year_of_birth = request.POST['birth_year']
        dob = '%s-%s-%s'%(year_of_birth, month_of_birth, day_of_birth)
        
        #Check that user exists
        if User.objects.filter(username__iexact=username).count()>0:
            return HttpResponse('A user with username %s already exists'%(username))

        if ClientAccount.objects.filter(email__iexact=email).count()>0:
            return HttpResponse('A user with email %s already exists'%(email))

        user_object = User.objects.create_user(username = username, password = password)
        AccountType.objects.create(user = user_object, individual = True)
        
        ClientAccount.objects.create(title = title, first_name = first_name, last_name = last_name, email = email,
                                     gender = gender, dob = dob, user = user_object)

        authenticated_user = auth.authenticate(username = username, password = password)

        if authenticated_user is not None:
            auth.login(request, authenticated_user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')
    
        
        
    return HttpResponse('Something went wrong :(')

def create_company_account(request):

    if request.POST:
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        name = request.POST['name']
        description = request.POST['description']

        #Check that user exists
        if User.objects.filter(username__iexact=username).count()>0:
            return HttpResponse('A user with username %s already exists'%(username))

        if CompanyAccount.objects.filter(email__iexact=email).count()>0:
            return HttpResponse('A user with email %s already exists'%(email))

        user_object = User.objects.create_user(username = username, password = password)
        AccountType.objects.create(user = user_object, company = True)
        
        CompanyAccount.objects.create(title = name, description = description, email = email, user = user_object)

        authenticated_user = auth.authenticate(username = username, password = password)

        if authenticated_user is not None:
            auth.login(request, authenticated_user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')

    
    return HttpResponse('Something went wrong :(')

def create_insurance_company(request):

    if request.POST:
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        name = request.POST['name']
        description = request.POST['description']

        #Check that user exists
        if User.objects.filter(username__iexact=username).count()>0:
            return HttpResponse('A user with username %s already exists'%(username))

        if InsuranceCompanyAccount.objects.filter(email__iexact=email).count()>0:
            return HttpResponse('A user with email %s already exists'%(email))

        user_object = User.objects.create_user(username = username, password = password)
        AccountType.objects.create(user = user_object, insurance_provider = True)
        
        InsuranceCompanyAccount.objects.create(title = name, description = description, email = email, user = user_object)

        authenticated_user = auth.authenticate(username = username, password = password)

        if authenticated_user is not None:
            auth.login(request, authenticated_user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')



    return HtppResponse('Something went wrong :(')

def create_medical_account(request):

    if request.POST:
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        name = request.POST['name']
        description = request.POST['description']

        #Check that user exists
        if User.objects.filter(username__iexact=username).count()>0:
            return HttpResponse('A user with username %s already exists'%(username))

        if MedicalAgentAccount.objects.filter(email__iexact=email).count()>0:
            return HttpResponse('A user with email %s already exists'%(email))

        user_object = User.objects.create_user(username = username, password = password)
        AccountType.objects.create(user = user_object, medical_institution = True)
        
        MedicalAgentAccount.objects.create(title = name, description = description, email = email, user = user_object)

        authenticated_user = auth.authenticate(username = username, password = password)

        if authenticated_user is not None:
            auth.login(request, authenticated_user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')


    
    return HttpResponse('Something went wrong :(')

def create_police_account(request):

    if request.POST:
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        name = request.POST['name']
        description = request.POST['description']

        #Check that user exists
        if User.objects.filter(username__iexact=username).count()>0:
            return HttpResponse('A user with username %s already exists'%(username))

        if PoliceAgentAccount.objects.filter(email__iexact=email).count()>0:
            return HttpResponse('A user with email %s already exists'%(email))

        user_object = User.objects.create_user(username = username, password = password)
        AccountType.objects.create(user = user_object, police_station = True)
        
        PoliceAgentAccount.objects.create(title = name, description = descriptio, email = email, user = user_object)

        authenticated_user = auth.authenticate(username = username, password = password)

        if authenticated_user is not None:
            auth.login(request, authenticated_user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')


    
    return HttpResponse('Something went wrong :(')

def create_service_agent_account(request):

    if request.POST:
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        name = request.POST['name']
        description = request.POST['description']

        #Check that user exists
        if User.objects.filter(username__iexact=username).count()>0:
            return HttpResponse('A user with username %s already exists'%(username))

        if ServiceAgentAccount.objects.filter(email__iexact=email).count()>0:
            return HttpResponse('A user with email %s already exists'%(email))

        user_object = User.objects.create_user(username = username, password = password)
        AccountType.objects.create(user = user_object, service_agent = True)
        
        ServiceAgentAccount.objects.create(title = name, description = description, email = email, user = user_object)

        authenticated_user = auth.authenticate(username = username, password = password)

        if authenticated_user is not None:
            auth.login(request, authenticated_user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')


    
    return HttpResponse('Something went wrong :(')
