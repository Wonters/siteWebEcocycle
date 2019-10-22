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

def salamandre(request):
    homeview.increaseGites()
    return render(request, 'home/salamandre.html')

def vente(request):
    # à développer le template quand il y aura des produits à vendre
    return render(request, 'home/vente.html')

def galery(request):
    homeview.increaseGalery()
    galerys = Galery.objects.all()
    photos = Photo.objects.all()
    return render(request,'home/galery.html', {'galerys': galerys,'photos':photos})

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
        send_mail('AcTI contact', form.cleaned_data['user_message'], form.cleaned_data['user_email'],
                  ['tristan.herou@gmail.com'], fail_silently=False, )
        form.save()
        print("debug: saved name contact ", form.cleaned_data['user_name'])
        for i in Contact.objects.all():
            if str(i) == form.cleaned_data['user_email']:
                Contact.objects.filter(user_email=str(i)).delete()
                form.save()
        return render(request, 'home/remerciement.html')
    else:
        print('form Contact is not valide')
        return render(request, 'home/contact.html')

