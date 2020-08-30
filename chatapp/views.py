# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User
# Create your views here.

def intro(request, userExisted=False):
    print(userExisted)
    return render(request,"intro.html",{'userExisted':userExisted})

def chat(request):
    username = request.POST['username']
    try:
        User.objects.get(name = username)
        # return redirect('intro', userExisted=True)
        return render(request, "intro.html", {"userExisted":True})
    except Exception as e:
        print(e)
    user = User(name=username)
    # 여기에 유저 속성정보를 추가하십시오
    user.save()
    return render(request,"chat.html",{'user':user})