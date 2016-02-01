# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import login_view, logout_view


app_name = 'loginlogout'

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
]
