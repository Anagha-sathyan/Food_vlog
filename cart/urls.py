from django.urls import path
from . import views
urlpatterns = [
    path('CartDetails',views.cart_details,name='CartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('cart_decrement/<int:product_id>/', views.min_cart, name='cart_decrement'),
    path('remove/<int:product_id>/', views.remove_cart, name='remove')
]