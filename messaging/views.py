from django.shortcuts import render
from rest_framework import viewsets
from messaging.models import Message
from messaging.serializers import MessageSerializer
from rest_framework.response import Response

# Create your views here.


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer