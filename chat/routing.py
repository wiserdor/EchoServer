from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]

router = routers.DefaultRouter()
router.register(r'echo', views.EchoView, base_name='echo')
router.register(r'broadcast', views.BroadcastView, base_name='broadcast')

http_urlpatterns = [
    path('', include(router.urls)),
]