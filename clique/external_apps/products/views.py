from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *

def product_index(request):
    pass
    
def product_show(request, product_id):
    product = Product.objects.get(id = product_id)
    return render_to_response('products/show.html', {'product' : product})
