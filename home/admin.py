from django.contrib import admin

from .models import Galery, Photo, Homestatistics
# Register your models here.


admin.site.register(Photo)
admin.site.register(Galery)
admin.site.register(Homestatistics)
