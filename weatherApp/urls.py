from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('/', TemplateView.as_view(template_name='home.html'), name='home'),

]
