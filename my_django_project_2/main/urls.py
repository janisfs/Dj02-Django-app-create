from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),   # главная страница сайта 'home'
    path('about/', views.about, name='about'),  # страница 'about'
]
