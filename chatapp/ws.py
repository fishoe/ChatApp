# -*- coding:utf-8 -*-
import json

from django.shortcuts import render, redirect
from django.urls import reverse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json

from .utils import checkHateWord



usersoc = []

async def chatting(scope,receive,send):
    
    model = load_model("../model")
    tokenizer = None
    tokens = ""
    with open("../tokenizer_euckr.json", "r", encoding="euc-kr") as f:
        tokens = json.loads(f.readlines()[0])
        tokenizer = tokenizer_from_json(tokens)
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
            count, score = await checkHateWord(name, model, tokenizer, msg)
            send = {"name":name, "msg":msg, "count":count, "score":score}
            send = json.dumps(send)
            for soc in usersoc:
                await soc({
                    'type':'websocket.send',
                    # 'text':name+ " 님 : " + text + "  !경고!" + count + "회" ,
                    'text': send
                })
                
        else :
            pass


