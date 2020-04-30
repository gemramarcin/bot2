from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage),
    path('output', views.external, name="script"),
    path('index', views.index),
    path('packetGen', views.packetGen),
    path('help', views.help),
    path('scenario', views.scenario),
]