from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage),
    path('output', views.external, name="script"),
    path('packetGen', views.packetGen),
    path('help', views.help),
    path('scenario', views.scenario),
]