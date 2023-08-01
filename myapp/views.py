from .models import About, Services, Portfolio
from .form import PortfolioForm, NewContact,AboutForm,ServiceForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def index(request):
    abouts = About.objects.all()
    services = Services.objects.all()
    portfolios = Portfolio.objects.all()
    if request.method == 'GET':
        return render(request, 'index.html', {
            'abouts' : abouts,
            'services' : services,
            'portfolios' : portfolios,
            'form': NewContact
        })
    else:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email_template.html', {
            'name' : name,
            'email' : email,
            'message' : message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['kcandres21@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Se ha enviado tu correo')
        return redirect('index')

def salir(request):
    logout(request)
    return redirect('index')

@login_required
def administrador(request):
    abouts = About.objects.all()
    services = Services.objects.all()
    portfolios = Portfolio.objects.all()
    return render(request, 'admin/administrador.html',{
        'abouts' : abouts,
        'services' : services,
        'portfolios' : portfolios
    })

class List_abouts(View):
    def get(self, request):
        abouts = About.objects.all()
        return render(request,'admin/about/index.html',{'abouts' : abouts})

class Create_about(CreateView):
    model = About
    form_class = AboutForm
    template_name = 'admin/about/add_about.html'

    def get_success_url(self):
        return reverse('about')

class Update_about(UpdateView):
    model = About
    form_class = AboutForm
    template_name='admin/about/add_about.html'
    success_url = reverse_lazy('about')

class Delete_about(DeleteView):
    model = About
    success_url = reverse_lazy("about")



class List_services(View):
    def get(self, request):
        services = Services.objects.all()
        return render(request,'admin/service/index.html',{'services' : services})
    
class Create_service(CreateView):
    model = Services
    form_class = ServiceForm
    template_name = 'admin/service/add_service.html'

    def get_success_url(self):
        return reverse('service')

class Update_service(UpdateView):
    model = Services
    form_class = ServiceForm
    template_name='admin/service/add_service.html'
    success_url = reverse_lazy('service')

class Delete_service(DeleteView):
    model = Services
    success_url = reverse_lazy("service")




class List_portfolios(View):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        return render(request,'admin/portfolio/index.html',{'portfolios' : portfolios})
    
class Create_portfolio(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'admin/portfolio/add_portfolio.html'

    def get_success_url(self):
        return reverse('portfolio')

class Update_portfolio(UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name='admin/portfolio/add_portfolio.html'
    success_url = reverse_lazy('portfolio')

class Delete_portfolio(DeleteView):
    model = Portfolio
    success_url = reverse_lazy("portfolio")