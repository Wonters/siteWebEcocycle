from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('gouvernance', gouvernance, name='salamandre'),
    path('envoieContact', envoie_contact, name='envoie'),
    path('recherche', recherche),
    path('galery', galery),
    path('declarationfondateur', declarationsFondateurs),
    path('vision-missions', visionMissions),
    path('adhesion', adhesion),
    path('calendrier', calendrier),
    path('dons', dons),
]
