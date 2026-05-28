from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('', views.home, name='home'),# главная страница 
    path('rozclad-zanatiy/', views.rozclad_zanatiy, name='rozclad-zanatiy'),# страница расписаните занятий 
    path('price-steel-puma/', views.price_steel_puma, name='price-steel-puma'),# страниц цены клуба
    path('team-steel-puma/', views.team, name='team-steel-puma'),# команда фитнес клуба 
]
