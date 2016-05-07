from django.db import models

class Conversation(models.Model):
	title=models.CharField(max_length=255)

class Sender(models.Model):
    nickname=models.CharField(max_length=255, unique=True)
    conversations=models.ManyToManyField(Conversation)

class Message(models.Model):
    text=models.TextField()
    date=models.DateTimeField()
    sender=models.ForeignKey(Sender)
    conversation=models.ForeignKey(Conversation)

