from django.urls import path

from . import views

app_name = 'story3'

urlpatterns = [
    path('', views.index, name='index'),
    path('/interest.html', views.index, name='interest'),
    path('/aboutme.html', views.index, name='aboutme'),
    path('/gallery.html', views.index, name='gallery'),
    path('/credits.html', views.index, name='credits'),
]