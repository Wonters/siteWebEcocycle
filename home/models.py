from django.db import models

# Create your models here.

class Homestatistics(models.Model):
    home_click = models.FloatField()
    acti_click = models.IntegerField()
    giteChambreDhote_click = models.IntegerField()
    like_click = models.IntegerField()
    contact_click = models.IntegerField()
    galery_click = models.IntegerField()

    def __init__(self):
        self.home_click = 0
        self.acti_click = 0
        self.giteChambreDhote_click = 0
        self.like_click = 0
        self.contact_click = 0
        self.galery_click = 0

    def increaseHome(self):
         self.home_click += 1

    def increaseActi(self):
        self.acti_click += 1

    def increaseGites(self):
        self.giteChambreDhote_click += 1

    def increaselike(self):
        self.like_click += 1

    def increaseContact(self):
        self.contact_click += 1

    def increaseGalery(self):
        self.galery_click += 1

###############

class Contact(models.Model):
    user_name = models.TextField(null=True)
    user_email = models.EmailField()
    user_phone = models.DecimalField(max_digits=10, decimal_places=1)
    user_message = models.TextField(null=True)

    def __str__(self):
        return self.user_name


class Photo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    img = models.ImageField(blank=True, null=True, upload_to="galery/%Y/%m/%D/")

    def __str__(self):
        return self.title

# à changer --> une galery, plusieurs photos qui font référence à un post du blog
## Ne fonctionne pas, proplème de selection des photos manyTomany
class Galery(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return self.title

class Categorie(models.Model): # AcTI, ALL, Ecoquartier
    type = models.CharField(max_length=100)

class AdhesionAssciation(models.Model): # membree actif, usagers et bienfaiteurs
    type = models.CharField(max_length=40, default='usager')
    prix = models.IntegerField(default=0)

class Member(models.Model): # nom, photo, description, membre, catégorie
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    img_profil = models.ImageField(blank=True, null=True, upload_to="team/")
    adhesion = models.ForeignKey(AdhesionAssciation, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default='acti')

class Team(models.Model): # regroupe tous les membres d'une catégorie
    member = models.ForeignKey(Member, on_delete = models.CASCADE)


    def filter(self):
        categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)



