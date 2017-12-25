import datetime

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import *
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login

from django.middleware import csrf
# Create your views here.


@login_required(login_url='/watsapp/login/')
def users(request):

    users_list = User.objects.order_by('id').exclude(username__exact=request.user.username)
    template = loader.get_template('MsgApp/users.html')

    context = {'users_list': users_list}

    return HttpResponse(template.render(context))


@login_required(login_url='/watsapp/login/')    #watsapp/3/
@csrf_protect
def message(request, user_id):
    messages = Message.objects.filter(sender_id=user_id).filter(receiver_id=request.user.id).\
        __or__(Message.objects.filter(sender_id=request.user.id).filter(receiver_id=user_id))
    messages = messages.order_by('pub_date')
    somethings = Message.objects.filter()
    template = loader.get_template('MsgApp/messages.html')
    context = {'messages_list': messages,'user_id':user_id,'user_fullname':User.objects.filter(id=user_id).first()}
    return HttpResponse(template.render(context))


@login_required(login_url='/watsapp/login/')
#@csrf_protect
@csrf_exempt
def send(request, user_id):
    newMessage = Message()
    newMessage.content = request.POST.get('new_message')
    newMessage.sender = request.user
    newMessage.receiver = User.objects.filter(id=user_id).first()
    newMessage.pub_date = datetime.datetime.now()
    newMessage.save()
    return redirect('/watsapp/'+user_id+'/')


@csrf_protect
@csrf_exempt
def login_view(request):
    template = loader.get_template('registration/login.html')
    login(request)
    return HttpResponse(template)


#@login_required(login_url='/watsapp/login/')
@csrf_protect
def logout_view(request, user_id):
    logout(request)
    return redirect('/watsapp/login/')