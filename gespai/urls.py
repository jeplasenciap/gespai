"""gespai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
import notifications.urls

from . import forms

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', include('upload.urls')),
    url(r'^cambios/', include('cambios.urls')),
    url(r'^personal/', include('personal.urls')),
    url(r'^administracion/', include('administracion.urls')),
    url(r'^responsables/', include('responsables.urls')),
    url(r'^$', TemplateView.as_view(template_name='gespai/index.html'), name='index'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^login/$', auth_views.login, {'authentication_form': forms.LoginForm}),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}),
    url('^', include('django.contrib.auth.urls'))
]
