# -*- coding: utf-8 -*-
from datetime import datetime, date
from random import randint

from rest.models import *
from django.core.management.base import BaseCommand

conversation_count = 50
sender_count = 50
message_per_conversation = 10

class Command(BaseCommand):
    def handle(self, *args, **options):
        for sender_id in range(1, sender_count + 1):
            sender = Sender(nickname="Sender #%d" % sender_id)
            sender.save()
            self.stdout.write("Sender #%d" % sender_id)

        for conversation_id in range(1, conversation_count + 1):
            conversation = Conversation(title="Conversation #%d" % conversation_id)
            conversation.save()
            self.stdout.write("Conversation #%d" % conversation_id)

            for i in range(1, message_per_conversation + 1):
                sender = Sender.objects.get(pk=randint(1, sender_count))

                message = Message(text="Message #%d" % i,
                                  date=datetime.now(),
                                  sender=sender,
                                  conversation=conversation)
                message.save()
                sender.conversations.add(conversation)
                sender.save()
                self.stdout.write("Message #%d per conver #%d" % (i, conversation_id))
