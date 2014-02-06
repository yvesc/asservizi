# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.template import Context
from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404
from models import Page, Categoria, Galleria, Allegati, Documento, Image
from django.http import HttpResponseRedirect

from contact_form import views, forms
from contact_form.forms import *
from contact_form.views import *

from django.db.models import Q



class HomeView(ListView):
    queryset = Page.objects.all()
    queryset = Page.objects.filter(categoria_id=1)
    template_name = 'sicurezza.html'

class SicurezzaView(ListView):
    queryset = Page.objects.filter(categoria_id=1)
    context_object_name = 'page_list'
    template_name = 'sicurezza.html'

class AmbienteView(ListView):
    queryset = Page.objects.filter(categoria_id=2)
    context_object_name = 'page_list'
    template_name = 'ambiente.html'

class FormazioneView(ListView):
    queryset = Page.objects.filter(categoria_id=3)
    context_object_name = 'page_list'
    template_name = 'formazione.html'

class OrganizazzioneView(ListView):
    queryset = Page.objects.filter(categoria_id=4)
    context_object_name = 'page_list'
    template_name = 'organizazzione.html'

class PraticheView(ListView):
    queryset = Page.objects.filter(categoria_id=5)
    context_object_name = 'page_list'
    template_name = 'pratiche.html'

class PerizieView(ListView):
    queryset = Page.objects.filter(categoria_id=6)
    context_object_name = 'page_list'
    template_name = 'perizie.html'

class PageView(DetailView):
    queryset = Page.objects.all()
    context_object_name = 'page'
    template_name = 'pagina.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(PageView, self).get_context_data(**kwargs)
        ciao = Page.objects.all()
        context['allegati_list'] = Allegati.objects.filter(allegato=context['page'].id)
        context['galleria_list'] = Galleria.objects.filter(pagina=context['page'].id)
        context['form2'] = BasicContactForm
        return context

class ProblematicaView(ListView):
    queryset = Page.objects.all()
    context_object_name = 'page_list'
    template_name = 'problematica.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(ListView, self).get_context_data(**kwargs)
        #ciao = Page.objects.all()
        #context['allegati_list'] = Allegati.objects.filter(allegato=context['page'].id)
        #context['galleria_list'] = Galleria.objects.filter(pagina=context['page'].id)
        context['form2'] = BasicContactForm
        return context

class RichiestaView(ListView):
    queryset = Page.objects.all()
    context_object_name = 'page_list'
    template_name = 'richiesta.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(ListView, self).get_context_data(**kwargs)
        #ciao = Page.objects.all()
        #context['allegati_list'] = Allegati.objects.filter(allegato=context['page'].id)
        #context['galleria_list'] = Galleria.objects.filter(pagina=context['page'].id)
        context['form2'] = BasicContactForm
        return context

# CONTATTI
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            subject = form.cleaned_data['subject']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            tel = form.cleaned_data['tel']
            fax = form.cleaned_data['fax']
            mail = form.cleaned_data['mail']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['pierangelo1982@gmail.com']
            if cc_myself:
                recipients.append(sender)

        from django.core.mail import send_mail
        send_mail(subject, address, city, tel, fax, mail, message, sender, recipients)
        return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })


'''

def search(request):
    try:
        q = request.GET['q']
        posts = Page.objects.filter(titolo__search=q) | \
                Page.objects.filter(intro__search=q) | \
                Page.objects.filter(body__search=q)
        return render_to_response('results.html', {'posts':posts, 'q':q})
    except KeyError:
        return render_to_response('results.html')