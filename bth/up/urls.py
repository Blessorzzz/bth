from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('api/similar-products/', views.get_similar_products, name='similar_products'),  
]
