import simplejson as json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers 
from models import *
import models as m

def index(request):
    if(request.method == 'GET'):
        return render_to_response('core/index.html')
        
def association_test(request):
    if(request.method == 'GET'):
        return render_to_response('core/association-test.html')
        
def content_association(request):
    if(request.method == 'GET'):
        items = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in Product.objects.all()]
        json_serializer = serializers.get_serializer("json")()
        #items_json = json_serializer.serialize(items, ensure_ascii = False)
        items_json = json.dumps(items)
        return HttpResponse(items_json)
    elif(request.method == 'POST'):
        # Insert association.
        source_item = request.POST['source_item'].split('-')
        item = request.POST['item'].split('-')
        source_model = source_item[0]
        source_model_id = source_item[1]
        target_model = item[0]
        target_model_id = item[1]
        content_association = ContentAssocation.objects.get_or_create(source_model = source_model, source_model_id = source_model_id, target_model = target_model, target_model_id = target_model_id)[0]
        content_association.target_model_count += 1

        # Get real target model so that we can store it's URL.
        target_model_klass = getattr(m, target_model.capitalize())
        target_model_instance = target_model_klass.objects.get(pk = target_model_id)
        content_association.target_model_link = target_model_instance.get_absolute_url()
        content_association.save()
        json_serializer = serializers.get_serializer("json")()
        return HttpResponse(json.dumps(dict(target_model_link = content_association.target_model_link, target_model_link_class = content_association.target_model_link_class, target_model = content_association.target_model)))

