# coding=utf-8

from django.conf.urls import patterns, include, url
from jproject.views import *


urlpatterns = patterns('',
    url(r'^project_list/$', project_list),
    url(r'^project_add/$', project_add),
    url(r'^project_detail/$', project_detail),
)