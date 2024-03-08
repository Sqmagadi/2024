from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('sale/', views.sale, name='sale'),
    path('new/', views.new, name='new'),
    path('featured/', views.featured, name='featured'),
    path('offers/', views.offers, name='offers'),
    path('search/', views.search, name='search'),
]