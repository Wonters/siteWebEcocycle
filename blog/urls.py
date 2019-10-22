from django.urls import path

from .views import *

urlpatterns = [
    path('', accueil, name='accueil'),
    path('article/<int:id>', lire, name='lire'),
    path('pdf', pdf, name='pdf'),
]