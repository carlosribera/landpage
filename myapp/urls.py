from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name="index"),
    path('salir', views.salir, name="salir"),
    path('administrador', views.administrador, name="administrador"),

    path('portfolio',login_required(views.List_portfolios.as_view()), name='portfolio'),
    path('portfolio/create',login_required(views.Create_portfolio.as_view()),name='create-portfolio'), 
    path('edit-portfolio/<int:pk>',login_required(views.Update_portfolio.as_view()), name='edit-portfolio'),
    path('delete_portfolio/<int:pk>',login_required(views.Delete_portfolio.as_view()), name='delete-portfolio'),
]
