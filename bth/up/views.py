from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
import math
from django.templatetags.static import static

def index(request):
    return render(request, 'index.html')

# API 
def get_similar_products(request):
    if request.method == 'GET':
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        c = float(request.GET.get('c', 0))
        d = float(request.GET.get('d', 0))

        products = Product.objects.all()
        results = []
        for product in products:
            distance = math.sqrt(
                (product.sour - a) ** 2 +
                (product.sweet - b) ** 2 +
                (product.bitter - c) ** 2 +
                (product.spicy - d) ** 2
            )
            image_url = static(product.image) 
            results.append({
                'name': product.name,
                'distance': distance,
                'image': image_url,
                'attributes': {
                    'sour': product.sour,
                    'sweet': product.sweet,
                    'bitter': product.bitter,
                    'spicy': product.spicy
                }
            })
        
        results = sorted(results, key=lambda x: x['distance'])[:4]
        return JsonResponse({'products': results})
