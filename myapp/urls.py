from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name="index"),
    path('salir', views.salir, name="salir"),
    path('administrador', views.administrador, name="administrador"),

    path('about',login_required(views.List_abouts.as_view()), name='about'),
    path('about/create',login_required(views.Create_about.as_view()), name='create-about'),
    path('edit-about/<int:pk>',login_required(views.Update_about.as_view()), name='edit-about'),
    path('delete-about/<int:pk>',login_required(views.Delete_about.as_view()), name='delete-about'),

    
    path('service',login_required(views.List_services.as_view()), name='service'),
    path('service/create',login_required(views.Create_service.as_view()),name='create-service'), 
    path('edit-service/<int:pk>',login_required(views.Update_service.as_view()), name='edit-service'),
    path('delete-service/<int:pk>',login_required(views.Delete_service.as_view()), name='delete-service'),

    path('portfolio',login_required(views.List_portfolios.as_view()), name='portfolio'),
    path('portfolio/create',login_required(views.Create_portfolio.as_view()),name='create-portfolio'), 
    path('edit-portfolio/<int:pk>',login_required(views.Update_portfolio.as_view()), name='edit-portfolio'),
    path('delete_portfolio/<int:pk>',login_required(views.Delete_portfolio.as_view()), name='delete-portfolio'),


]
