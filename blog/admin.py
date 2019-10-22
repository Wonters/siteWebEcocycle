from django.contrib import admin

# Register your models here.


from .models import Article, Pdf

admin.site.register(Article)
admin.site.register(Pdf)
