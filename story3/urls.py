from django.urls import path

from . import views

app_name = 'story3'

urlpatterns = [
    path('', views.index, name='index'),
    path('/interest.html', views.interest, name='interest'),
    path('/aboutme.html', views.aboutme, name='aboutme'),
    path('/gallery.html', views.gallery, name='gallery'),
    path('/credits.html', views.credits, name='credits'),
]