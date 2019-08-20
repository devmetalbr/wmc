# -*- coding: utf-8 -*-
# @Filename : urls
# @Date : 2019-08-19-19-24
# @Poject: wmc
# @AUTHOR : Christian Douglas <christian.douglas.alcantara@gmail.com>
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
