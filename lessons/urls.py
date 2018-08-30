from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('add_questions/', views.add_questions),
    path('progress/', views.progress_view, name='progress'),
    path('<str:qid>/', views.question, name='question'),
    re_path(r'^$', views.index, name='index'),
]
