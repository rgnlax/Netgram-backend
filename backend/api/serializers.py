from api.models import *
from rest_framework import serializers

class UnixEpochDateField(serializers.DateTimeField):
    def to_representation(self, value):
        """ Return epoch time for a datetime object or ``None``"""
        import time
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None

    def to_internal_value(self, value):
        import datetime
        return datetime.datetime.fromtimestamp(int(value))

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'title')

class SenderSerializer(serializers.ModelSerializer):
    conversations = ConversationSerializer(many=True)
    class Meta:
        model = Sender
        fields = ('id', 'nickname', 'conversations')

class MessageSerializer(serializers.ModelSerializer):
    date = UnixEpochDateField()
    class Meta:
        model = Message
        fields = ('id', 'text', 'date', 'sender', 'conversation')