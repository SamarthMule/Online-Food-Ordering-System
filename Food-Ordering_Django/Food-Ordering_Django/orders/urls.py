from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.landingpage, name='landingpage'),  # Landing page at the root URL
    path('home/', views.home, name='home'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register, name='register'),
    path('pizza/', views.pizza, name='pizza'),
    path('pasta/', views.pasta, name='pasta'),
    path('salad/', views.salad, name='salad'),
    path('subs/', views.subs, name='subs'),
    path('dinner_platters/', views.dinner_platters, name='dinner_platters'),
    path('directions/', views.directions, name='directions'),
    path('hours/', views.hours, name='hours'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('view-orders/', views.view_orders, name='view_orders'),
    path('mark_order_as_delivered/', views.mark_order_as_delivered, name='mark_order_as_delivered'),
    path('save_cart/', views.save_cart, name='save_cart'),
    path('retrieve_saved_cart/', views.retrieve_saved_cart, name='retrieve_saved_cart'),
    path('check_superuser/', views.check_superuser, name='check_superuser'),
    path('makepayment/', views.makepayment, name='makepayment'),
    path('review/', views.review, name='review'),
    path('user_details/', views.user_details, name='user_details'),
    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
    path('term/', views.term, name='term'),
    path('work_with_us/',views.work_with_us, name='work_with_us'),
    path('privacy/', views.privacy, name='privacy'),
    path('about/', views.about, name='about')
]
