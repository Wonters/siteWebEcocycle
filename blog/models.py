from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    img = models.ImageField(blank=True, null=True, upload_to="blog/article/%Y/%m/%D/")
    date = models.DateField(default=timezone.now,
                                verbose_name="Date de parution")

    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.titre


class Pdf(models.Model):
    titre = models.CharField(max_length=100)
    pdfFile = models.FileField(blank=True, null=True, upload_to="blog/pdf/%Y/%m/%D/")

    class Meta:
        verbose_name = "pdf"

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.titre