from django.urls import path
from shop import views

from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from shop.sitemap import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}

app_name = 'shop'



urlpatterns = [
    path('', views.home, name='home'),# главная страница 
    path('rozclad-zanatiy/', views.rozclad_zanatiy, name='rozclad-zanatiy'),# страница расписаните занятий 
    path('price-steel-puma/', views.price_steel_puma, name='price-steel-puma'),# страниц цены клуба
    path('team-steel-puma/', views.team, name='team-steel-puma'),# команда фитнес клуба 
    path('galery-steel-puma/', views.galery, name='galery-steel-puma'),#галерея фитнес клуба 
    path('rules-steel-puma/', views.rules, name='rules-steel-puma'),#галерея фитнес клуба
    path('news-steel-puma/', views.news, name='news-steel-puma'),#галерея фитнес клуба

    
    path("llms.txt",views.llms_txt, name="llms_txt"),#llms txt
    path("robots.txt",views.robots_txt, name="robots_txt"),#robots txt
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),#sitemap.xml
    

]
