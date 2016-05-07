from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from rest.views import *

router = DefaultRouter()

router.register(r'conversations', ConversationViewSet)
router.register(r'sender', SenderViewSet)
router.register(r'message', MessageViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'login/', LoginView.as_view()),
)
