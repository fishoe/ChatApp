# -*- coding:utf-8 -*-
import json

from django.shortcuts import render, redirect
from django.urls import reverse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import os
from pathlib import Path
from .utils import checkHateWord

modelpath = Path(os.getcwd()).parent
print(modelpath)
usersoc = []
model1 = load_model("saved_model/model1")
model2 = load_model("saved_model/model2")
model = [model1,model2]
tokenizer = None
tokens = ""
with open("tokenizer.json", "r", encoding="euc-kr") as f:
    tokens = json.loads(f.readlines()[0])
    tokenizer = tokenizer_from_json(tokens)

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
            count, score = await checkHateWord(name, model, tokenizer, msg)
            print(count,score)
            if score > 0.5 :
                packet = {"score":str(score),'status':'mute',"count":str(count)}
                packet = json.dumps(packet)
                await send({
                    'type':'websocket.send',
                    'text':packet
                })
                continue
            packet = {"name":name, "msg":msg, "count":str(count), "score":str(score),'status':'text'}
            packet = json.dumps(packet)
            for soc in usersoc:
                print(soc)
                await soc({
                    'type':'websocket.send',
                    # 'text':name+ " 님 : " + text + "  !경고!" + count + "회" ,
                    'text': packet
                })
                
        else :
            pass


