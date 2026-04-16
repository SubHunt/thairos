from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('beer/', views.beer_brands, name='beer_brands'),
    path('juice/', views.juice_brands, name='juice_brands'),
    path('juice/<slug:slug>/', views.juice_brand_detail, name='juice_brand_detail'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.brand_detail, name='brand_detail'),
]
