from django.urls import path
from . import views

app_name = "tienda"

# 2 TEMPLATE -> 3 URL
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.productsByCategory, name='productsByCategory'),
    path('product/<int:product_id>', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('addCart/<int:product_id>', views.addCart, name='addCart'),
    path('deleteCart/<int:product_id>', views.deleteCart, name='deleteCart'),
    path('clearCart', views.clearCart, name='clearCart'),
    path('login', views.loginUser, name='login'),
    path('profile', views.acountUsers, name='profile'),
    path('createUser', views.createUser, name='createUser'),
]
