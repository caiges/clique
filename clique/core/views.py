import simplejson as json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers 
from models import *

def index(request):
    if(request.method == 'GET'):
        return render_to_response('core/index.html')
        
def association_test(request):
    if(request.method == 'GET'):
        return render_to_response('core/association-test.html')
        
def item_association(request):
    if(request.method == 'GET'):
        items = Product.objects.all()
        json_serializer = serializers.get_serializer("json")()
        items_json = json_serializer.serialize(items, ensure_ascii = False)
        return HttpResponse(items_json)
    elif(request.method == 'POST'):
        # Insert association.
        print request.post
        return HttpResponse(request.post)
