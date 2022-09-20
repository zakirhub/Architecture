import email
from email import message
from unicodedata import name
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from architecture.models import Contact, Project, AboutMe, AboutUs, SliderImage
from django.contrib import messages

# Create your views here.

def homeView(request):
    project = Project.objects.order_by('-date')[:6]
    aboutme = AboutMe.objects.all()
    slider = SliderImage.objects.all()
    return render(request, 'architecture/index.html', {'project':project, 'me':aboutme, 'slider':slider})

def AboutusView(request):
    aboutus = AboutUs.objects.all()
    return render(request, 'architecture/about.html', {'us':aboutus})

def contactView(request):
    if request.method == 'POST':
            nm = request.POST['name']
            em = request.POST['email']
            ph = request.POST['phone']
            mg = request.POST['message']
            form = Contact(name=nm, email=em, phone=ph, message=mg)
            form.save()
            messages.success(request, 'Thank You! We will contact you soon')
            print(messages)
    return render(request, 'architecture/contact.html', )

def myprojectsView(request):
    project = Project.objects.all()
    return render(request, 'architecture/myprojects.html', {'project':project})

class DetailView(DetailView):
    model = Project
    template_name = 'architecture/detail.html'
    def get_context_data(self, **kwargs):
         context =  super().get_context_data(**kwargs)
         context['all'] = self.model.objects.all().order_by('title')
         return context

