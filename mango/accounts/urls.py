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
    url(r'^registration/$',views.registration, name = 'registration'),
    url(r'^create_individual/$',views.create_individual_account, name = 'create_individual'),
    url(r'^create_company/$',views.create_company_account, name = 'create_company'),
    url(r'^create_medical/$',views.create_medical_account, name = 'create_medical'),
    url(r'^create_police/$',views.create_police_account, name = 'create_police'),
    url(r'^create_service_agent/$',views.create_service_agent_account, name = 'create_service_agent'),
    ]
