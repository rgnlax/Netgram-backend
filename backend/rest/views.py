# -*- coding: utf-8 -*-
import datetime
import hashlib
from rest.models import *
from rest.serializers import *
from rest_framework import mixins, viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request):
        try:
            nickname = request.data['nickname']
            sender, created = Sender.objects.get_or_create(nickname=nickname)
            return Response({'user': SenderSerializer(sender).data, 'created': created})
        except:
            return Response({'error': 'Nickname is required'})

class ConversationViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = Conversation.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('sender',)
    serializer_class = ConversationSerializer

class SenderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer

class MessageViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('sender', 'conversation')

    def create(self, request):
        if (hashlib.md5(request.data["text"]).hexdigest() == request.data["checksum"]):
            message = Message(text=request.data["text"],
                              date=datetime.datetime.fromtimestamp(int(request.data["date"])),
                              sender_id=request.data["sender_id"],
                              conversation_id=request.data["conversation_id"])
            message.save()
            return Response({"Status": "Ok"})
        else:
            return Response({"Status": "Ne Ok"})
