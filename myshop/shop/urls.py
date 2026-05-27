from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('', views.home, name='home'),
    path('rozclad-zanatiy/', views.rozclad_zanatiy, name='rozclad-zanatiy'),
    path('price-steel-puma/', views.price_steel_puma, name='price-steel-puma'),
]
