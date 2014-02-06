# Create your views here.
from django.contrib import admin
from sito.models import Page, Categoria, Allegati, Documento, Galleria, Image 
from image_cropping import ImageCroppingMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Page, MyModelAdmin)
admin.site.register(Allegati, MyModelAdmin)
admin.site.register(Documento, MyModelAdmin)
admin.site.register(Image, MyModelAdmin)
admin.site.register(Galleria, MyModelAdmin)
admin.site.register(Categoria, MyModelAdmin)
