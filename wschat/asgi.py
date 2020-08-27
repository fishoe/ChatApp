"""
ASGI config for wschat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wschat.settings')

application = get_asgi_application()

from chatapp.ws import chatting

async def wsproc(scope, receive, send):
    if scope["type"] == 'http' :
        await application(scope,receive,send)
    elif scope["type"] == 'websocket':
        await chatting(scope,receive,send)
    else :
        raise NotImplementedError(f"Unknown scope type {scope['type']}")