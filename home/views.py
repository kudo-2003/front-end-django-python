from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Product


def home(request):
    return render(request, 'index.html')

def product_detail(request, product_id):
    product = get_object_or_404()
    return render(request, 'product_detail.html', {'product': product})

