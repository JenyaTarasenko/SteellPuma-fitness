from django.shortcuts import render


def home(request):
    return render(request, 'shop/product/home.html')

def rozclad_zanatiy(request):
    return render(request, 'shop/product/rozclad-zanatiy.html')
    
    

def price_steel_puma(request):
    return render(request, 'shop/product/price.html')

def team(request):
       return render(request, 'shop/product/team.html')
    



