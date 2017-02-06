from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.


class MessageObject(object):
    user = None
    last_sent = None
    message = None
    sender = None

    def __init__(self, userObject, lastSentDate, lastMessage):
        self.user = userObject
        self.last_sent = lastSentDate
        self.message = lastMessage


class AdminMessage(View):
    def get(self, request, **kwargs):
        messageForm = MessageForm()
        messages = Message.objects.all()
        context = {}
        context["messageForm"] = messageForm
        if messages:
            adminmessage = User.objects.get(username="adminmessage")
            messageObjectList = []
            userlist = []
            for indMessage in messages:
                if indMessage.sender == adminmessage:
                    if indMessage.recipient not in userlist:
                        messageObject = MessageObject(
                            indMessage.recipient,
                            indMessage.created_at,
                            indMessage.body)
                        messageObjectList.append(messageObject)
                        userlist.append(indMessage.recipient)
                else:
                    if indMessage.sender not in userlist:
                        messageObject = MessageObject(
                            indMessage.sender,
                            indMessage.created_at,
                            indMessage.body)
                        messageObjectList.append(messageObject)
                        userlist.append(indMessage.sender)
            context["messageObjectList"] = messageObjectList
        if "slug" not in kwargs.keys():
            message = Message.objects.all().first()
            adminmessage = User.objects.get(username="adminmessage")
            userName = None
            if message.sender == adminmessage:
                userName = message.recipient.username
            else:
                userName = message.sender.username

            return HttpResponseRedirect("/messages/admin/{}".format(userName))
        else:
            userSlug = kwargs["slug"]
            user = User.objects.get(username=userSlug)
            userMessages = Message.objects.filter(
                sender=user) | Message.objects.filter(recipient=user)
            context["userMessages"] = userMessages
            context["user"] = user
            return render(request, "messaging/adminMessage.html", context)

    def post(self, request, **kwargs):
        messageForm = MessageForm(request.POST or None)
        userSlug = kwargs["slug"]
        user = User.objects.get(username=userSlug)
        adminmessage = User.objects.get(username="adminmessage")
        if messageForm.is_valid():
            message = messageForm.save(commit=False)
            message.sender = adminmessage
            message.recipient = user
            message.save()
            return HttpResponseRedirect("/messages/admin/{}".format(userSlug))
        messages = Message.objects.all()
        context = {}
        context["messageForm"] = messageForm
        if messages:
            messageObjectList = []
            userlist = []
            for indMessage in messages:
                if indMessage.sender == adminmessage:
                    if indMessage.recipient not in userlist:
                        messageObject = MessageObject(
                            indMessage.recipient,
                            indMessage.created_at,
                            indMessage.body)
                        messageObjectList.append(messageObject)
                        userlist.append(indMessage.recipient)
                else:
                    if indMessage.sender not in userlist:
                        messageObject = MessageObject(
                            indMessage.sender,
                            indMessage.created_at,
                            indMessage.body)
                        messageObjectList.append(messageObject)
                        userlist.append(indMessage.sender)
            context["messageObjectList"] = messageObjectList
        userMessages = Message.objects.filter(
            sender=user) | Message.objects.filter(recipient=user)
        context["userMessages"] = userMessages
        context["user"] = user
        return render(request, "messaging/adminMessage.html", context)
