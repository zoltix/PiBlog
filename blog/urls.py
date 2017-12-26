""" django 3.0 qui a du être adaptée"""
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.accueil, name='accueil'),
    #re_path(r'^(?P<slug>.+)$', views.lire_article, name='blog_lire'),
    path('blog/<slug:slug>/', views.lire_article, name='blog_lire'),
]

