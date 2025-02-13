from django.contrib import admin
from django.urls import path
from store.views import home, products, shoes, coats, tshirts, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('products/shoes/', shoes, name='shoes'),
    path('products/coats/', coats, name='coats'),
    path('products/tshirts/', tshirts, name='tshirts'),
    # path('About Us/', About Us, name='About Us'),
    path('contact/', contact, name='contact'),
]
