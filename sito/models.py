from django.db import models
from tinymce import models as tinymce_models
from image_cropping import ImageRatioField, ImageCropField


# Create your models here.

class Image(models.Model):
    image_field = models.ImageField(upload_to='uploaded_images')

class Documento(models.Model):
    documento = models.FileField(upload_to='uploaded_documenti')

class Page(models.Model):
    titolo = models.CharField(max_length=200)
    #body = tinymce_models.HTMLField()
    body = tinymce_models.HTMLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    cropping = ImageRatioField('image', '140x140')
    pub_date = models.DateTimeField('date published')

    def __unicode__ (self):
        return self.titolo

class Allegati(models.Model):
    titoloallegato = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True, null=True)
    sezione = models.ForeignKey(Page)
    allegato = models.ForeignKey(Documento)
    pub_date = models.DateTimeField('date published')

    def __unicode__ (self):
        return self.titoloallegato

class Galleria(models.Model):
    gallerianome = models.CharField(max_length=200)
    pagina = models.ForeignKey(Page)
    image = models.ForeignKey(Image)
    cropping = ImageRatioField('image__image_field', '700x500')
    croppingthumb = ImageRatioField('image__image_field', '350x213')
    
    def __unicode__ (self):
        return unicode(self.gallerianome)  
    

