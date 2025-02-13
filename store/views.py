from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')


def shoes(request):
    return render(request, 'productss/shoes.html')


def coats(request):
    return render(request, 'productss/coats.html')


def tshirts(request):
    return render(request, 'productss/tshirts.html')

# def About_Us(request):
  #   return render(request, 'About_Us.html')

def contact(request):
    return render(request, 'contact.html')

   
