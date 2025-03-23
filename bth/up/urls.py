from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 根路径渲染 index.html
    path('api/similar-products/', views.get_similar_products, name='similar_products'),  # API 端点
]
