"""Trombinoscoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from Trombinoscoop import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.publications),
    path('login/', views.login),
    path('addFriend/', views.add_friend),
    path('showProfile', views.show_profile),
    path('modifyProfile', views.modify_profile),
    path('ajax/checkEmailField', views.ajax_check_email_field),
    path('ajax/checkEmaField', views.ajax_check_email_field),
    path('ajax/addFriend', views.ajax_add_friend),
    path('register/', views.register)
]
