from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('', views.home, name='home'),
    path('rozclad-zanatiy/', views.rozclad_zanatiy, name='rozclad-zanatiy'),
]
