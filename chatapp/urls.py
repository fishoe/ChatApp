from . import views
from django.urls import path

urlpatterns = [
    path('', views.intro, name = 'intro'),
    path('chat/', views.chat, name = 'chat'),
]
