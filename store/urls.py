from django.urls import path
from . import views

urlpatterns = [
path('', views.store, name ='store' ),
path('cart/' , views.cart, name = 'cart'),
path('aboutus/' , views.aboutus, name = 'aboutus'),
path('checkout/' , views.checkout, name = 'checkout'),
path('products/' , views.products, name = 'products'),
#
# path('update_item/', views.updateItem, name="update_item"),
# path('process_order/', views.processOrder, name="process_order"),
]
