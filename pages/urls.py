from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('beer/', views.beer_brands, name='beer_brands'),
    path('juice/', views.juice_brands, name='juice_brands'),
    path('juice/<slug:slug>/', views.juice_brand_detail, name='juice_brand_detail'),
    path('snacks/', views.snacks_landing, name='snacks_landing'),
    path('about/', views.about, name='about'),
    path('where-to-buy/', views.where_to_buy, name='where_to_buy'),
    path('terms/', views.terms, name='terms'),
    path('<slug:slug>/', views.brand_detail, name='brand_detail'),
]
