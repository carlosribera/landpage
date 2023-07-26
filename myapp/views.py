from django.http.response import HttpResponseRedirect
from .models import About, Services, Portfolio
from django.shortcuts import render, redirect
from .form import PortfolioForm, NewContact
from django.urls import reverse
from django.views import View
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

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


def administrador(request):
    abouts = About.objects.all()
    services = Services.objects.all()
    portfolios = Portfolio.objects.all()
    return render(request, 'admin/administrador.html',{
        'abouts' : abouts,
        'services' : services,
        'portfolios' : portfolios
    })


class SavePortfolio(View):
    def get(self, request):
        form = PortfolioForm()
        return render(request, 'portfolio/saveportfolio.html', {
            "form": form
        })

    def post(self, request):
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administrador'))


# def add_portfolio(request):
#     if request.method == 'GET':
#         # show interface
#         return render(request, 'add_portfolio.html', {
#             'form': createNewPorfolio()
#         })
#     else:
#         Portfolio.objects.create(
#             title=request.POST['title'], 
#             description=request.POST['description'], 
#             image=request.POST['image'])
#         return redirect('portfolio')