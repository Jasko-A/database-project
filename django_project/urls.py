"""django_project URL Configuration

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
from django.contrib.auth import views as auth_views

from jokerank import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # our apps
    url(r'^', include('stats.urls', namespace='stats')),
    url(r'^jokes/', include('jokerank.urls', namespace='jokerank')),
    # url(r'^jokerank/', include('jokerank.urls', namespace='jokerank')),
    # url(r'^jokerank/main-page', views.get_main, name='get_main'),

    # signup/login/logout
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'jokerank/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/logout/success/'}, name='logout'),
    url(r'^logout/success/$', views.logout_success, name='logout_success'),
]