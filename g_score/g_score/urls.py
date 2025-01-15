"""
URL configuration for g_score project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from scores import views    

urlpatterns = [
    path('', views.home_view, name='home'),
    path('score-check/', views.score_check_view, name='score_check'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('top-students/', views.top_students_view, name='top_students'),
]