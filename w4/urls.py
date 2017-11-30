"""w4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from contact.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Main.as_view()),
    url(r'^show/(?P<person_id>(\d)+$)', show_person),
    url(r'^modify/(?P<person_id>(\d)+$)', modify_person),
    url(r'^person/new$', AddEditPerson.as_view()),
    url(r'^person/modify/(?P<person_id>(\d)+$)', AddEditPerson.as_view()),
    url(r'^delete/(?P<person_id>(\d)+$)', delete_person),
    url(r'^person/(?P<person_id>(\d)+)/address/add$', AddEditAddress.as_view()),
    url(r'^person/(?P<person_id>(\d)+)/address/(?P<address_id>(\d)+)/modify$', AddEditAddress.as_view()),
    url(r'^person/(?P<person_id>(\d)+)/address/(?P<address_id>(\d)+)/delete/$', delete_address),
    url(r'^person/(?P<person_id>(\d)+)/telephone/add$', AddEditTelephone.as_view()),
    url(r'^person/(?P<person_id>(\d)+)/telephone/(?P<telephone_id>(\d)+)/modify$', AddEditTelephone.as_view()),
    url(r'^person/(?P<person_id>(\d)+)/telephone/(?P<telephone_id>(\d)+)/delete/$', delete_telephone),
    url(r'^person/(?P<person_id>(\d)+)/email/add$', AddEditEmail.as_view()),
    url(r'^person/(?P<person_id>(\d)+)/email/(?P<email_id>(\d)+)/modify$', AddEditEmail.as_view()),
    url(r'^person/(?P<person_id>(\d)+)/email/(?P<email_id>(\d)+)/delete/$', delete_email),
    url(r'^person/(?P<person_id>(\d)+)/group/add', AddToGroup.as_view()),
    url(r'^person/(?P<person_id>(\d)+)/group/create', CreateGroup.as_view()),
    url(r'^person/(?P<person_id>(\d)+)/group/(?P<group_id>(\d)+)/remove/$', remove_from_group),
]
