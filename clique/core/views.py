import simplejson as json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers 
from products.models import *

def index(request):
    if(request.method == 'GET'):
        return render_to_response('core/index.html')
        
def association_test(request):
    if(request.method == 'GET'):
        return render_to_response('core/association-test.html')
        
def product_association(request):
    if(request.method == 'GET'):
        products = Product.objects.all()
        json_serializer = serializers.get_serializer("json")()
        products_json = json_serializer.serialize(products, ensure_ascii = False)
        return HttpResponse(products_json)
    elif(request.method == 'POST'):
        # Insert association.
        pass
