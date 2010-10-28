import simplejson as json
import uuid

from django.shortcuts import render_to_response
from django.http import HttpResponse
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
        items_json = json.dumps(items)
        return HttpResponse(items_json)
    elif(request.method == 'POST'):
        # Insert/Update association.
        source_item = request.POST['source_item'].split('-')
        item = request.POST['item'].split('-')
        source_model = source_item[0]
        source_model_id = source_item[1]
        target_model = item[0]
        target_model_id = item[1]
        target_model_field = request.POST['model_field']
        target_model_link_name = str(uuid.uuid4()) if request.POST['link_name'].strip() == '' else request.POST['link_name'].strip()
        content_association = ContentAssociation.objects.get_or_create(target_model_link_name = target_model_link_name)[0]
        content_association.source_model = source_model
        content_association.source_model_id = source_model_id
        content_association.target_model = target_model
        content_association.target_model_id = target_model_id
        content_association.target_model_field = target_model_field
                
        # Get real target model so that we can store it's URL.
        target_model_klass = getattr(m, target_model.capitalize())
        target_model_instance = target_model_klass.objects.get(pk = target_model_id)
        content_association.target_model_link = target_model_instance.get_absolute_url()
        content_association.save()
        
        return HttpResponse(json.dumps(dict(target_model_link = content_association.target_model_link, target_model_link_name = content_association.target_model_link_name, target_model = content_association.target_model)))
        
def remove_content_association(request):
    if(request.method == 'POST'):
        link_name = request.POST['link_name']
        content_association = ContentAssociation.objects.filter(target_model_link_name__exact = link_name)
        content_association.delete()
        return HttpResponse("Content association removed")

