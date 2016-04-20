from time import mktime
from api.models import *
from api.serializers import *
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