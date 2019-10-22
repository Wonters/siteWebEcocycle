from django.contrib import admin

# Register your models here.

from .models import EvenementsCulturel,EvenementsFablab, PassBureaux, AbonnementsFablab, Produit

@admin.register(EvenementsCulturel)
class EvenementsCulturelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
@admin.register(EvenementsFablab)
class EvenementsFablabAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
@admin.register(AbonnementsFablab)
class AbonnementsFablabAdmin(admin.ModelAdmin):
    list_display = ('type', 'prix')
@admin.register(PassBureaux)
class PassBureauxAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')