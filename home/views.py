from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse

from .forms import ContactForm

from .models import Contact, Galery, Photo, Homestatistics

homeview = Homestatistics()

def home(request):
    homeview.increaseHome()
    return render(request, 'home/home.html', {'like': homeview.like_click})

def contact(request):
    homeview.increaseContact()
    return render(request, 'home/contact.html')

def gouvernance(request):
    return render(request, 'home/gouvernance.html')

def recherche(request):
    # à développer, arriver des données par le backend sigfox
    return render(request, 'home/recherche.html')

def visionMissions(request):
    return render(request, 'home/vision-missions.html')

def galery(request):
    homeview.increaseGalery()
    galerys = Galery.objects.all()
    photos = Photo.objects.all()
    return render(request, 'home/galery.html', {'galerys': galerys, 'photos': photos})

def declarationsFondateurs(request):
    return render(request, 'home/fondateurs.html')

def adhesion(request):
    return render(request, 'home/adhesion.html')

def calendrier(request):
    return render(request, 'home/calendrier.html')
def dons(request):
    return  render(request, 'home/dons.html')

def like(request):
    if request.is_ajax():
        homeview.increaselike()
        return JsonResponse({'nblike':homeview.like_click})
    return HttpResponse("Error Ajax")


def envoie_contact(request):
    print('debug: form Contact')
    print('debug: request.method=post')
    form = ContactForm(request.POST)
    if form.is_valid():
        send_mail('EcoCycle contact', form.cleaned_data['user_message'], form.cleaned_data['user_email'],
                  ['ecocycle.domaine.salamandre@gmail.com'], fail_silently=False, )
        form.save()
        print("debug: saved name contact ", form.cleaned_data['user_name'])
        for i in Contact.objects.all():
            if str(i) == form.cleaned_data['user_email']:
                Contact.objects.filter(user_email=str(i)).delete()
                form.save()
        return render(request, 'home/contact.html', {'envoie':True})
    else:
        print('form Contact is not valide')
        return render(request, 'home/contact.html')

