from django.shortcuts import render


def home(request):
    return render(request, 'shop/product/home.html')

def rozclad_zanatiy(request):
    return render(request, 'shop/product/rozclad-zanatiy.html')
    
    





