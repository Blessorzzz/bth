"""
URL configuration for bth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('up.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# #    Product(name='Pickled Fish', sour=100, sweet=80, bitter=0, spicy=40, image='static/img/pickled_fish.jpg'),
#     Product(name='Orange', sour=70, sweet=95, bitter=10, spicy=0, image='static/img/orange.jpg'),
#     Product(name='Bitter Melon', sour=0, sweet=10, bitter=95, spicy=10, image='static/img/bitter_melon.jpg'),
#     Product(name='Spicy Noodles', sour=20, sweet=30, bitter=5, spicy=90, image='static/img/spicy_noodles.jpg'),
#     Product(name='Lemon Candy', sour=85, sweet=60, bitter=5, spicy=0, image='static/img/lemon_candy.jpg'),
#     Product(name='Chili Chocolate', sour=10, sweet=70, bitter=20, spicy=50, image='static/img/chili_chocolate.jpg'),
#     Product(name='Salted Plum', sour=90, sweet=40, bitter=15, spicy=5, image='static/img/salted_plum.jpg'),
#     Product(name='Honey Cake', sour=5, sweet=100, bitter=0, spicy=0, image='static/img/honey_cake.jpg'),
#     Product(name='Wasabi Peas', sour=10, sweet=20, bitter=30, spicy=80, image='static/img/wasabi_peas.jpg'),
#     Product(name='Grapefruit', sour=75, sweet=50, bitter=25, spicy=0, image='static/img/grapefruit.jpg'),