from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('salamandre', salamandre, name='salamandre'),
    path('envoieContact', envoie_contact, name='envoie'),
    path('vente', vente),
    path('galery', galery),
    path('like', like)
]
