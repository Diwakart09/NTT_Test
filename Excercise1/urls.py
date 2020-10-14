"""Excercise1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import interface_details.views as det_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',det_views.create_view),
    path('<id>/',det_views.detail_view),
    path('<id>/update/',det_views.update_view),
    path('<id>/delete/',det_views.delete_view)
]
