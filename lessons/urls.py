from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<qid>/', views.question),
    re_path(r'^$', views.index),
]
