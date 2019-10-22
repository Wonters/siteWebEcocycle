from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    Produits = Produit()
    EvenementsCulturels = EvenementsCulturel()
    EvenementsFablabs = EvenementsFablab()
    PassBureauxs = PassBureaux()
    AbonnementsFablabs =AbonnementsFablab()
    evenementsCulturels = EvenementsCulturels._getEvenementsCulturel()
    evenementsFablabs = EvenementsFablabs._getEvenementsFablab()
    passBureauxs = PassBureauxs._getPassBureaux()
    abonnementsFablabs = AbonnementsFablabs._getAbonnementsFablab()
    produits = Produits._getProduit()

    return render(request, 'acti/acti.html', {'produits': produits,'abonnements':abonnementsFablabs,'pass':passBureauxs,
                                              'eventsCulturel':evenementsCulturels,'eventsFablab':evenementsFablabs})