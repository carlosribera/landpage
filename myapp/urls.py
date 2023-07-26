from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('administrador', views.administrador, name="administrador"),
    path('saveportfolio', views.SavePortfolio.as_view(), name="add-portfolio"),
]
