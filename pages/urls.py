from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('beer/', views.beer_brands, name='beer_brands'),
    path('<slug:slug>/', views.brand_detail, name='brand_detail'),
]
