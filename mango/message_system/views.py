from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from products.models import Policy
from message_system.models import Message
from django.db.models import Q

# Create your views here.
def view_inbox(request):

    messages = Message.objects.filter(receiver = request.user).order_by('date_sent')
    args = {}
    args['messages'] = messages
    args['page_type'] = 'inbox'
    return render_to_response('messages.html',args)

def view_outbox(request):
    messages = Message.objects.filter(sender = request.user).order_by('date_sent')
    args = {}
    args['messages'] = messages
    args['page_type'] = 'outbox'
    return render_to_response('messages_outbox.html',args)

def view_message(request):

    message_id = request.GET.get('message_id')
    message = Message.objects.get(id = message_id)

    if message.sender != request.user and message.receiver != request.user:
        return HttpResponse('You are not allowed to view this message')

    args = {}
    args.update(csrf(request))
    args['message'] = message

    return render_to_response('view_message.html',args)

def ask_question(request):

    try:
        if request.POST:
            message = request.POST['message']
            policy_id = request.GET.get('policy_id')
            policy_id = int(policy_id)
            policy = Policy.objects.get(id=policy_id)
            insurance_company_user = policy.insurance_company.user
            subject = 'Question about %s'%(policy.title)
            
            Message.objects.create(sender = request.user, receiver = insurance_company_user,
                                   body = message, subject = subject)
            return HttpResponseRedirect('/insurance/policy/?policy_id=%s'%policy_id)
        
        policy_id = request.GET.get('policy_id')
        policy = Policy.objects.get(id = policy_id)
        
        args = {}
        args.update(csrf(request))
        args['policy'] = policy
        return render_to_response('ask_question.html',args)
    except:
        
        return HttpResponse('Something went wrong :(')

def reply(request):

    if request.POST:
        message_id = request.GET.get('message_id')
        message = Message.objects.get(id=message_id)
        body = request.POST['message']

        subject = "Re: %s"%message.subject

        if message.sender == request.user:
            sender = request.user
            receiver = message.receiver
        else:
            sender = request.user
            receiver = message.sender
            

        Message.objects.create(sender = sender, receiver = receiver,
                               body = body, subject = subject)

        return HttpResponseRedirect('/messages/inbox/')
    else:
        return HttpResponse('Something went wrong :(')
