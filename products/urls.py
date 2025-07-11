from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    #category urls
    path('category/<slug:slug>/', views.products_by_category, name='products_by_category'),
]
