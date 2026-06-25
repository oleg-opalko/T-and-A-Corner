from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('category/<slug:slug>/', views.category_detail, name='category'),
    path('perfume/<slug:slug>/', views.perfume_detail, name='perfume_detail'),
]
