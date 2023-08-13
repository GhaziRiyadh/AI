from django.urls import re_path

from . import consumers

websocket_urlpattern = [
    re_path(r'api/user/video-streem', consumers.VideoConsumer.as_asgi())
]
