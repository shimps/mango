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
    url(r'^types/$',views.insurance_types, name = 'types'),
    url(r'^my/$',views.my_insurance, name = 'my_insurance'),
    url(r'^create_policy/$',views.create_policy, name = 'create_policy'),
    url(r'^policy/$',views.view_policy, name = 'view_policy'),
    url(r'^apply/upload_files/$',views.upload_application_files, name='upload_application_files'),
    url(r'^apply/$',views.apply_for_policy, name = 'apply_for_policy'),
    url(r'application/continue/$',views.continue_policy_application, name = 'continue_policy_application'),
    url(r'^claims/$',views.view_claims, name = 'view_claims'),
    url(r'^make_claim/$',views.make_claim, name = 'make_claim'),
    url(r'^claim/continue/$',views.continue_claim, name = 'continue_claim'),
    url(r'^claim/upload_files/$',views.upload_claim_files, name = 'upload_claim_files'),
    url(r'^apply/save/$',views.save_application, name = 'save_application'),
    url(r'^policies/$',views.view_policies, name = 'view_policies'),
    url(r'^payment_options/$',views.view_payment_options, name = 'view_payment_options'),
    ]
