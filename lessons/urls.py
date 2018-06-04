from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('add_questions/', views.add_questions),
    path('<str:qid>/', views.question),
    re_path(r'^$', views.index),
]
