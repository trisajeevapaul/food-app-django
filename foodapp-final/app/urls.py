from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"), 
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('menu/', views.menu, name='menu'),
    path('order/<int:item_id>/', views.order_item, name='order_item'),
    path('orders/', views.view_orders, name='view_orders'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]