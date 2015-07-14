"""pm URL Configuration

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
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pm.views.index'),
    url(r'^api/user/$', 'pm.api.api_user'),
    url(r'^skin_config/$', 'pm.views.skin_config'),
    url(r'^install/$', 'pm.views.install'),
    url(r'^base/$', 'pm.views.base'),
    url(r'^login/$', 'pm.views.login'),
    url(r'^logout/$', 'pm.views.logout'),
    url(r'^file/upload/$', 'pm.views.upload'),
    url(r'^file/download/$', 'pm.views.download'),
    url(r'^error/$', 'pm.views.httperror'),
    url(r'^juser/', include('juser.urls')),
    url(r'^jasset/', include('jasset.urls')),
    url(r'^jlog/', include('jlog.urls')),
    url(r'^jperm/', include('jperm.urls')),
    url(r'^node_auth/', 'pm.views.node_auth'),
]
