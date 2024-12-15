import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Fetch all products
def get_all_products(request):
    products = list(Product.objects.values())
    return JsonResponse({"status": "success", "data": products}, safe=False)

# Create a new product
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(name=data['name'], price=data['price'])
        return JsonResponse({
            "status": "success",
            "data": {
                "id": product.id,
                "name": product.name,
                "price": float(product.price)
            }
        })
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


#auth
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secure_data(request):
    return JsonResponse({"status": "success", "data": "Secure data"})
