from django.db import models
from tinymce import models as tinymce_models
from image_cropping import ImageRatioField, ImageCropField
from django import forms
from django.forms import widgets
from django.forms import ModelForm, Textarea


# Create your models here.

class Image(models.Model):
    image_field = models.ImageField(upload_to='uploaded_images')

class Documento(models.Model):
    documento = models.FileField(upload_to='uploaded_documenti')

class Categoria(models.Model):
    categoria = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__ (self):
        return self.categoria

class Page(models.Model):
    titolo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    #body = tinymce_models.HTMLField()
    body = tinymce_models.HTMLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    cropping = ImageRatioField('image', '500x136')
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
    cropping = ImageRatioField('image__image_field', '660x300')
    croppingthumb = ImageRatioField('image__image_field', '350x213')
    
    def __unicode__ (self):
        return unicode(self.gallerianome) 

'''# CONTACT

class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'contactform'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'contactform'}))
    city = subject = forms.CharField(widget=forms.TextInput(attrs={'class':'contactform'}))
    tel = subject = forms.CharField()
    fax = subject = forms.CharField(widget=forms.TextInput(attrs={'class':'contactform'}))
    mail = subject = forms.CharField(widget=forms.TextInput(attrs={'class':'contactform'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'contactform'}))
    sender = forms.CharField(widget=forms.TextInput(attrs={'class':'contactform'}))
    cc_myself = forms.BooleanField(required=False) 


'''