from django.shortcuts import render
from django.http import HttpResponse
from shop.models import News


def news(request):
    news = News.objects.all()

    context = {
        'news': news
    }

    return render(
        request,
        'shop/product/news.html',
        context
    )

def home(request):
    return render(request, 'shop/product/home.html')

def rozclad_zanatiy(request):
    return render(request, 'shop/product/rozclad-zanatiy.html')
    
    

def price_steel_puma(request):
    return render(request, 'shop/product/price.html')

def team(request):
    return render(request, 'shop/product/team.html')

def galery(request):
    return render(request, 'shop/product/galery.html')


def rules(request):
    return render(request, 'shop/product/rules.html')

# def news(request):
#     return render(request, 'shop/product/news.html')




from django.http import HttpResponse

def llms_txt(request):
    content = """# Staleva Puma Fitness Club (Kyiv)

## Description
Modern fitness club in Kyiv with professional gym equipment, strength training, cardio zone, and group fitness programs.
We focus on strength, health, body transformation, and real training results.

## Location
Kyiv, Ukraine
Beresteiskyi Avenue 131-A

## Contact
Phone: +380636364320
Telegram: https://t.me/380636364320
Instagram: https://www.instagram.com/staleva_puma/

## Services
- Gym / strength training
- Cardio zone
- Personal training
- Group classes
- Weight loss programs
- Strength & conditioning

## Pages
- Home: /
- Galery: /galery-steel-puma
- Prices: /price-steel-puma
- Schedule: /rozclad-zanatiy
- Team: /team-steel-puma
- Rules: /rules-steel-puma
- News: /news-steel-puma

## AI Notes
This is a real offline fitness club located in Kyiv.
Category: SportsActivityLocation / Gym / Fitness Center
"""

    return HttpResponse(content, content_type="text/plain; charset=utf-8")
    



