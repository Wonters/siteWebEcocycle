from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('calendrier', calendrier, name='calendrier'),
    path('ateliermobile', atelierMobile, name='atelier-mobile'),
]
