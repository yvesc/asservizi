# Create your views here.
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
#from django.views.generic import object_detail
#from django.views.generic import ListView
from sito import views
from contact_form import views, forms
from sito.views import HomeView, PageView, AmbienteView, FormazioneView, OrganizazzioneView, PraticheView, PerizieView, SicurezzaView, ProblematicaView, RichiestaView, SitoFeed
from sito.models import Page

from django.shortcuts import render, render_to_response, get_object_or_404

from views import search
#from django.contrib.syndication.views import Feed


urlpatterns = patterns('',
   url(r'^$', HomeView.as_view()),
   url(r'^ambiente$', AmbienteView.as_view()),
   url(r'^sicurezza$', SicurezzaView.as_view()),
   url(r'^formazione$', FormazioneView.as_view()),
   url(r'^organizazzione$', OrganizazzioneView.as_view()),
   url(r'^pratiche$', PraticheView.as_view()),
   url(r'^perizie$', PerizieView.as_view()),
   url(r'^pagina/(?P<pk>\d+)/$', PageView.as_view()),
   url(r'^contact/', include('contact_form.urls')),
   url(r'^problematica$', ProblematicaView.as_view()),
   url(r'^richiesta$', RichiestaView.as_view()),
   url(r'^results/$', 'sito.views.search'),
   url(r'^feed/$', SitoFeed()),
   #url(r'^([-_A-Za-z0-9]+)/$', views.dettaglio),
   #url(r'^pagine/(?P<pk>\d+)/$', PageView.as_view()),
  )

