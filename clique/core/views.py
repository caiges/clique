import simplejson as json
import uuid

from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *
import models as m

def index(request):
    if(request.method == 'GET'):
        return render_to_response('core/index.html')

def article_show(request, url):
    if(request.method == 'GET'):
        article = Article.objects.filter(url__exact = url, make_live__exact = True)
        return render_to_response('core/articles/show.html', {'article' : article})

def association_test(request):
    if(request.method == 'GET'):
        return render_to_response('core/association-test.html')

""" Product Categories """
def active_product_categories_list(request):
    if(request.method == 'GET'):
        product_categories = ProductCategory.objects.filter(product_categories__isnull = False).distinct()
        return render_to_response('core/product_categories/active_list.html', {'product_categories' : product_categories})
    
def product_categories_list(request):
    if(request.method == 'GET'):
        product_categories = ProductCategory.objects.all()
        athlete_product_categories = ProductCategory.objects.filter(product_categories__isnull = False, product_categories__for_athletes = True).distinct()
        return render_to_response('core/product_categories/list.html', {'product_categories' : product_categories, 'athlete_product_categories' : athlete_product_categories})

def product_category_show(request, product_category_name):
    if(request.method == 'GET'):
        product_category = ProductCategory.objects.filter(name__exact = product_category_name)[0]
        return render_to_response('core/product_categories/show.html', {'product_category' : product_category})
        
""" Products """
def product_show(request, product_id):
    if(request.method == 'GET'):
        product = Product.objects.get(pk = product_id)
        return render_to_response('core/products/show.html', {'product' : product})

def products_within_category(request, product_category_url):
    if(request.method == 'GET'):
        product_category = ProductCategory.objects.filter(url__exact = product_category_url)[0]
        products = Product.objects.filter(categories__exact = product_category)
        athlete_products = Product.objects.filter(categories__exact = product_category, for_athletes__exact = True)
        return render_to_response('core/products/list.html', {'category' : product_category, 'products' : products, 'athlete_products' : athlete_products})

def product_within_category_show(request, product_category_url, product_url):
    if(request.method == 'GET'):
        product_category = ProductCategory.objects.filter(url__exact = product_category_url)[0]
        product = Product.objects.filter(categories__exact = product_category, url__exact = product_url)[0]
        return render_to_response('core/products/show.html', {'category' : product_category, 'product' : product})

""" Content Association """ 
def content_association(request):
    if(request.method == 'GET'):
        articles = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in Article.objects.all()]
        exercises = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in Exercise.objects.all()]
        fitnesstips = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in FitnessTip.objects.all()]
        mythbusters = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in MythBuster.objects.all()]
        nutritiontips = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in NutritionTip.objects.all()]
        pages = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in Page.objects.all()]
        products = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in Product.objects.all()]
        recipes = [dict(model = p.__class__.__name__.lower(), id = p.id, name = p.name) for p in Recipe.objects.all()]
        items = dict(Articles = articles, Exercises = exercises, FitnessTips = fitnesstips, MythBusters = mythbusters, NutritionTips = nutritiontips, Pages = pages, Products = products, Recipes = recipes)
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
        target_model_link_id = str(uuid.uuid4()) if request.POST['link_id'].strip() == '' else request.POST['link_id'].strip()
        content_association = ContentAssociation.objects.get_or_create(target_model_link_id = target_model_link_id)[0]
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
        
        return HttpResponse(json.dumps(dict(target_model_link = content_association.target_model_link, target_model_link_id = content_association.target_model_link_id, target_model = content_association.target_model)))
        
def remove_content_association(request):
    if(request.method == 'POST'):
        link_id = request.POST['link_id']
        content_association = ContentAssociation.objects.filter(target_model_link_id__exact = link_id)
        content_association.delete()
        return HttpResponse("Content association removed")

