from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from accounts.models import InsuranceCompanyAccount, ClientAccount, CompanyAccount
from products.models import Policy, ClientPolicy, insurance_category_choices, Claim, AutoClaim, Application, AutoApplication
import datetime
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

def apply_for_policy(request):

    policy_id = request.GET.get('policy_id')
    policy = Policy.objects.get(id=policy_id)

    if request.POST:

        title = request.POST['title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        income = request.POST['income']
        funding_source = request.POST['funding_sources']
        funding_specify = request.POST['funding_specify']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        type_of_cover = request.POST['type_of_cover']
        vehicle_condition = request.POST['vehicle_condition']
        vehicle_make = request.POST['vehicle_make']
        vehicle_model = request.POST['vehicle_model']
        vehicle_seating_capacity = request.POST['vehicle_seating_capacity']
        vehicle_usage_area = request.POST['vehicle_usage_area']
        vehicle_usage_type = request.POST['vehicle_usage_type']
        
        application = Application.objects.create(title = title, first_name = first_name, last_name = last_name,
                                                 address = address, city = city, country = country, telephone = phone,
                                                 email_address = email, income = income, funding_sources = funding_sources,
                                                 funding_specify = funding_specify, auto_insurance = True, policy = policy, user = request.user)
        AutoApplication.objects.create(type_of_cover = type_of_cover, vehicle_condition = vehicle_condition, make = vehicle_make,
                                       model = vehicle_model, seating_capacity = vehicle_seating_capacity, vehicle_usage_area = vehicle_usage_area,
                                       vehicle_usage_type = vehicle_usage_type, application = application)
        
        return HttpResponseRedirect('/insurance/policy/?policy_id=%s'%policy_id)

    args = {}
    args.update(csrf(request))
    args['policy'] = policy
    
    return render_to_response('policy_apply.html',args)

def view_claims(request):
    args = {}
    return render_to_response('claims.html',args)

def make_claim(request):

    policy_id = request.GET.get('policy_id')
    policy = Policy.objects.get(id=policy_id)
    client = ClientAccount.objects.get(user = request.user)
    client_policy = ClientPolicy.objects.filter(policy = policy, client = client)[0]


    action = request.GET.get('action')

    if request.POST:
        #Insurance Holder Details
        title = request.POST['title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        phone = request.POST['phone']
        email = request.POST['email']
        #Payment Details
        payment_method = request.POST['payment_method']
        payment_details = request.POST['payment_details']
        #Vehicle Details
        vehicle_registration_number = request.POST['vehicle_registration_number']
        vehicle_make = request.POST['vehicle_make']
        vehicle_model = request.POST['vehicle_model']
        
        vehicle_registration_date = request.POST['vehicle_registration_date']
        if not vehicle_registration_date:
            vehicle_registration_date = None
        #Accident Details
        date_of_accident = request.POST['accident_date']
        if not date_of_accident:
            date_of_accident = None
            
        time_of_accident = request.POST['accident_time']
        if not time_of_accident:
            time_of_accident = None
            
        place_of_accident = request.POST['accident_place']
        #Police Station Details
        police_station = request.POST['police_station']
        garage = request.POST['garage']
        loss_estimate = request.POST['loss_estimate']
        number_in_vehicle = request.POST['number_in_vehicle']
        #Driver Details
        driver_name = request.POST['driver_name']
        
        dob_of_driver = request.POST['dob_of_driver']
        if not dob_of_driver:
            dob_of_driver = None
        
        license_no_of_driver = request.POST['license_number']
        
        license_expiry_of_driver = request.POST['license_expiry_date']
        if not license_expiry_of_driver:
            license_expiry_of_driver = None
        
        vehicle_authorization = request.POST['vehicle_authorization']
        #Other Insurance Companies
        insurance_company = request.POST['o_insurance_company']
        insurance_policy_number = request.POST['o_insurance_policy_number']
        
        insurance_start_date = request.POST['o_insurance_start_date']
        if not insurance_start_date:
            insurance_start_date = None
            
        insurance_end_date = request.POST['o_insurance_end_date']
        if not insurance_end_date:
            insurance_end_date = None
        

        if action == 'submit':
            claim = Claim.objects.create(title = title, first_name = first_name, last_name = last_name, address = address, city = city,
                                 country = country, telephone = phone, email_address = email, payment_method = payment_method,
                                 auto_insurance = True, submitted = True, policy = client_policy, user = request.user )
        elif action == 'save':
            claim = Claim.objects.create(title = title, first_name = first_name, last_name = last_name, address = address, city = city,
                                 country = country, telephone = phone, email_address = email, payment_method = payment_method,
                                 auto_insurance = True, submitted = False, policy = client_policy, user = request.user )

        AutoClaim.objects.create(registration_number = vehicle_registration_number, make = vehicle_make, model = vehicle_model,
                                 registration_date = vehicle_registration_date, date_of_accident = date_of_accident,
                                 time_of_accident = time_of_accident, police_station = police_station, garage_name = garage, loss_estimate = loss_estimate,
                                 number_in_vehicle = number_in_vehicle, name_of_driver = driver_name, dob_of_driver = dob_of_driver,
                                 license_number = license_no_of_driver, license_expiry_date = license_expiry_of_driver, vehicle_authorization = vehicle_authorization,
                                 o_insurance_company = insurance_company, o_insurance_policy_number = insurance_policy_number, o_insurance_start_date = insurance_start_date,
                                 o_insurance_end_date = insurance_end_date, claim = claim)
        

        
        return HttpResponse('/insurance/policy/?policy_id=%s'%policy_id)

    args = {}
    args.update(csrf(request))

    args['policy'] = policy
    args['client_policy'] = client_policy
    return render_to_response('make_claim.html',args)
            

def continue_claim(request):

    claim_id = request.GET.get('claim_id')
    claim = Claim.objects.get(id = claim_id)
    action = request.GET.get('action')
    
    if request.POST:
        
        #Insurance Holder Details
        title = request.POST['title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        phone = request.POST['phone']
        email = request.POST['email']
        #Payment Details
        payment_method = request.POST['payment_method']
        payment_details = request.POST['payment_details']
        #Vehicle Details
        vehicle_registration_number = request.POST['vehicle_registration_number']
        vehicle_make = request.POST['vehicle_make']
        vehicle_model = request.POST['vehicle_model']
        
        vehicle_registration_date = request.POST['vehicle_registration_date']
        if not vehicle_registration_date:
            vehicle_registration_date = None
        #Accident Details
        date_of_accident = request.POST['accident_date']
        if not date_of_accident:
            date_of_accident = None
            
        time_of_accident = request.POST['accident_time']
        if not time_of_accident:
            time_of_accident = None
            
        place_of_accident = request.POST['accident_place']
        #Police Station Details
        police_station = request.POST['police_station']
        garage = request.POST['garage']
        loss_estimate = request.POST['loss_estimate']
        number_in_vehicle = request.POST['number_in_vehicle']
        #Driver Details
        driver_name = request.POST['driver_name']
        
        dob_of_driver = request.POST['dob_of_driver']
        if not dob_of_driver:
            dob_of_driver = None
        
        license_no_of_driver = request.POST['license_number']
        
        license_expiry_of_driver = request.POST['license_expiry_date']
        if not license_expiry_of_driver:
            license_expiry_of_driver = None
        
        vehicle_authorization = request.POST['vehicle_authorization']
        #Other Insurance Companies
        insurance_company = request.POST['o_insurance_company']
        insurance_policy_number = request.POST['o_insurance_policy_number']
        
        insurance_start_date = request.POST['o_insurance_start_date']
        if not insurance_start_date:
            insurance_start_date = None
            
        insurance_end_date = request.POST['o_insurance_end_date']
        if not insurance_end_date:
            insurance_end_date = None

        if action == 'submit':
            '''
            claim.title = title
            claim.first_name = first_name
            claim.last_name = last_name
            claim.address = address
            claim.city = city
            claim.country = country
            claim.telephone = phone
            claim.email_address = email
            claim.payment_method = payment_method
            claim.auto_insurance = True
            claim.submitted = True
            claim.save()
            '''

            Claim.objects.update_or_create(id = claim.id, title = title, first_name = first_name, last_name = last_name, address = address, city = city,
                     country = country, telephone = phone, email_address = email, payment_method = payment_method,
                     auto_insurance = True, submitted = True)
            
        elif action == 'save':
            '''
            claim.title = title
            claim.first_name = first_name
            claim.last_name = last_name
            claim.address = address
            claim.city = city
            claim.country = country
            claim.telephone = phone,
            claim.email_address = email
            claim.payment_method = payment_method
            claim.auto_insurance = True
            claim.submitted = False
            claim.save()
            '''
            Claim.objects.update_or_create(id = claim.id,title = title, first_name = first_name, last_name = last_name, address = address, city = city,
                     country = country, telephone = phone, email_address = email, payment_method = payment_method,
                     auto_insurance = True, submitted = False)

        auto_claim = claim.auto_claim
        AutoClaim.objects.update_or_create(id=auto_claim.id, registration_number = vehicle_registration_number, make = vehicle_make, model = vehicle_model,
                         registration_date = vehicle_registration_date, date_of_accident = date_of_accident,
                         time_of_accident = time_of_accident, police_station = police_station, garage_name = garage, loss_estimate = loss_estimate,
                         number_in_vehicle = number_in_vehicle, name_of_driver = driver_name, dob_of_driver = dob_of_driver,
                         license_number = license_no_of_driver, license_expiry_date = license_expiry_of_driver, vehicle_authorization = vehicle_authorization,
                         o_insurance_company = insurance_company, o_insurance_policy_number = insurance_policy_number, o_insurance_start_date = insurance_start_date,
                         o_insurance_end_date = insurance_end_date)
        
        

        return HttpResponseRedirect('/in_progress/')

    args = {}
    args.update(csrf(request))

    args['claim'] = claim
    args['policy'] = claim.policy.policy
    
    return render_to_response('continue_claim.html',args)

def save_application(request):



    return HttpResponseRedirect('/insurance/my/')

def get_category_string(category_letter):
    for category in insurance_category_choices:
        if category[0] == category_letter:
            return category[1]
    return None

def my_insurance(request):

    current_policies = ClientPolicy.objects.filter(user = request.user)
    args = {}
    args['current_policies'] = current_policies
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

def view_payment_options(request):

    args = {}
    return render_to_response('payment_options.html',args)
    
