from django.db import models

from django.apps.config import import_module
# Create your models here.
import_module(name='home', package='ecocycle')

class Produit(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.IntegerField()
    description = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True, upload_to="acti/produits/")

    def _getProduit(self):
        listProduits = Produit.objects.all()
        return listProduits

class EvenementsCulturel(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.IntegerField()
    description = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True, upload_to="acti/produits/")

    def _getEvenementsCulturel(self):
        listEvenementsCulturel = EvenementsCulturel.objects.all()
        return listEvenementsCulturel

class EvenementsFablab(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.IntegerField()
    description = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True, upload_to="acti/produits/")

    def _getEvenementsFablab(self):
        listEvenementsFablab = EvenementsFablab.objects.all()
        return listEvenementsFablab


class AbonnementsFablab(models.Model):
    type = models.CharField(max_length=50)
    prix = models.IntegerField()
    description = models.CharField(max_length=100)

    def _getAbonnementsFablab(self):
        listAbonnements = AbonnementsFablab.objects.all()
        return listAbonnements

class PassBureaux(models.Model):
    nom=models.CharField(max_length=50)
    prix=models.IntegerField()
    description=models.CharField(max_length=200)

    def _getPassBureaux(self):
        listPass=PassBureaux.objects.all()
        return listPass


