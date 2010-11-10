from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *

def product_index(request):
    pass
    
def product_show(request, product_id):
    product = Product.objects.get(id = product_id, weider_for_athletes__exact = True)
    return render_to_response('products/show.html', {'product' : product})
