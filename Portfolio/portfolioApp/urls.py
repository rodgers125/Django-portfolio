from django.urls import path, include
from . import views

app_name = "portfolioApp"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.login, name='register')

]
