# -*- coding:utf-8 -*-
import json

from django.shortcuts import render, redirect
from django.urls import reverse

from .utils import checkHateWord



usersoc = []

async def chatting(scope,receive,send):
    while True :
        event = await receive()
        
        #handshake
        if event['type'] == "websocket.connect":
            usersoc.append(send)
            await send({
                'type': 'websocket.accept'
            })
        elif event['type'] == 'websocket.disconnet':
            usersoc.remove(send)
            break
        elif event['type'] == 'websocket.receive':
            msg = event['text']
            data = json.loads(msg)
            msg = data['text']
            name = data['id']
            count = await checkHateWord(name, msg)
            send = {"name":name, "msg":msg, "count":count}
            send = json.dumps(send)
            for soc in usersoc:
                await soc({
                    'type':'websocket.send',
                    # 'text':name+ " 님 : " + text + "  !경고!" + count + "회" ,
                    'text': send
                })
                
        else :
            pass


