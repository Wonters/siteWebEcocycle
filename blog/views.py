from django.shortcuts import render
from django.http import Http404

from .models import Article, Pdf

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/article.html', {'article': article})

def pdf(request):
    pdfFile = Pdf.objects.all()
    return render(request, 'blog/pdf.html', {'pdf': pdfFile})
