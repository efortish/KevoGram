"""Kevogram URLs module"""

#Django
from django.contrib import admin
from django.urls import path

#Kevogram
from kevogram import views as local_views
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("helloworld/", local_views.hello_world ),
    path("sorted/", local_views.sort_integers),
    path("hi/<str:name>/<int:age>/", local_views.say_hi),

    path('posts/', post_views.list_posts )
]
