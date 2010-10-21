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
        
def content_association(request):
    if(request.method == 'GET'):
        items = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in Product.objects.all()]
        print items
        json_serializer = serializers.get_serializer("json")()
        #items_json = json_serializer.serialize(items, ensure_ascii = False)
        items_json = json.dumps(items)
        return HttpResponse(items_json)
    elif(request.method == 'POST'):
        # Insert association.
        item = request.POST['item'].split('-')
        target_model = item[0]
        target_model_id = item[1]
        print "%s - %s" % (target_model, target_model_id)
        return HttpResponse(item)
