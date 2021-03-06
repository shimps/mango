"""mango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^inbox/$',views.view_inbox, name = 'view_inbox'),
    url(r'^outbox/$',views.view_outbox, name = 'view_outbox'),
    url(r'^view/$',views.view_message, name = 'view_message'),
    url(r'^ask/$',views.ask_question, name = 'ask_question'),
    url(r'^reply/$',views.reply, name = 'reply'),
    ]
