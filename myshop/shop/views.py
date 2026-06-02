from django.shortcuts import render


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

def news(request):
    return render(request, 'shop/product/news.html')

    



