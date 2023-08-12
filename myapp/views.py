from .models import Portfolio
from .form import PortfolioForm, NewContact
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
    portfolios = Portfolio.objects.all()
    if request.method == 'GET':
        return render(request, 'index.html', {
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
    portfolios = Portfolio.objects.all()
    return render(request, 'admin/administrador.html',{
        'portfolios' : portfolios
    })

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