from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.first_page, name="home"),
    path('best', views.best, name="best_page"),
    path('new', views.new, name="new_page"),
    path('hits', views.hits, name="hits_page"),
    path('images', views.images, name="images_page"),
    path('pornstar', views.pornstar, name="pornstar_page"),
    path('exclusive', views.exclusive, name="exclusive_page"),

]