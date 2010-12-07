import simplejson as json
import uuid

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from models import *
import models as m

def index(request):
    if(request.method == 'GET'):
        return render_to_response('core/index.html', {}, context_instance = RequestContext(request))

""" Article Categories """
def article_categories_list(request):
    if(request.method == 'GET'):
        article_categories = ArticleCategory.objects.filter(articles__isnull = False, language__exact = request.LANGUAGE_CODE).distinct()
        return render_to_response('core/article_categories/list.html', {'article_categories' : article_categories})

""" Articles """
def article_show(request, url):
    if(request.method == 'GET'):
        article = Article.objects.filter(url__exact = url, make_live__exact = True)
        return render_to_response('core/articles/show.html', {'article' : article})

def articles_within_category(request):
    if(request.method == 'GET'):
        categories = ArticleCategory.objects.filter(articles__isnull = False).distinct()
        return render_to_response('core/articles/list_by_category.html', {'categories' : categories})

def article_within_category_show(request, article_category_url, article_url):
    if(request.method == 'GET'):
        article_category = ArticleCategory.objects.filter(url__exact = article_category_url)[0]
        article = Article.objects.filter(categories__exact = article_category, url__exact = article_url)[0]
        return render_to_response('core/articles/show.html', {'article_category' : article_category, 'article' : article})

""" Exercise Categories """
def exercise_categories_list(request):
    if(request.method == 'GET'):
        exercise_categories = ExerciseCategory.objects.filter(exercises__isnull = False).distinct()
        return render_to_response('core/exercise_categories/list.html', {'exercise_categories' : exercise_categories})

""" Exercises """
def exercise_show(request, url):
    if(request.method == 'GET'):
        exercise = Exercise.objects.filter(url__exact = url, make_live__exact = True)
        return render_to_response('core/exercises/show.html', {'exercise' : exercise})

def exercises_within_category(request):
    if(request.method == 'GET'):
        categories = ExerciseCategory.objects.filter(exercises__isnull = False).distinct()
        return render_to_response('core/exercises/list_by_category.html', {'categories' : categories})

def exercise_within_category_show(request, exercise_category_url, exercise_url):
    if(request.method == 'GET'):
        exercise_category = ExerciseCategory.objects.filter(url__exact = exercise_category_url)[0]
        exercise = Exercise.objects.filter(categories__exact = exercise_category, url__exact = exercise_url)[0]
        return render_to_response('core/exercises/show.html', {'exercise_category' : exercise_category, 'exercise' : exercise})

""" Fitness Tip Categories """
def fitness_tip_categories_list(request):
    if(request.method == 'GET'):
        fitness_tip_categories = FitnessTipCategory.objects.filter(fitness_tips__isnull = False).distinct()
        return render_to_response('core/fitness_tip_categories/list.html', {'fitness_tip_categories' : fitness_tip_categories})

""" Fitness Tips """
def fitness_tip_show(request, url):
    if(request.method == 'GET'):
        fitness_tip = FitnessTip.objects.filter(url__exact = url, make_live__exact = True)
        return render_to_response('core/fitness_tips/show.html', {'fitness_tip' : fitness_tip})

def fitness_tips_within_category(request):
    if(request.method == 'GET'):
        categories = FitnessTipCategory.objects.filter(fitness_tips__isnull = False).distinct()
        return render_to_response('core/fitness_tips/list_by_category.html', {'categories' : categories})

def fitness_tip_within_category_show(request, fitness_tip_category_url, fitness_tip_url):
    if(request.method == 'GET'):
        fitness_tip_category = FitnessTipCategory.objects.filter(url__exact = fitness_tip_category_url)[0]
        fitness_tip = FitnessTip.objects.filter(categories__exact = fitness_tip_category, url__exact = fitness_tip_url)[0]
        return render_to_response('core/fitness_tips/show.html', {'fitness_tip_category' : fitness_tip_category, 'fitness_tip' : fitness_tip})

""" Myth Buster Categories """
def myth_buster_categories_list(request):
    if(request.method == 'GET'):
        myth_buster_categories = MythBusterCategory.objects.filter(myth_busters__isnull = False).distinct()
        return render_to_response('core/myth_buster_categories/list.html', {'myth_buster_categories' : myth_buster_categories})

""" Myth Busters """
def myth_buster_show(request, url):
    if(request.method == 'GET'):
        myth_buster = MythBuster.objects.filter(url__exact = url, make_live__exact = True)
        return render_to_response('core/myth_busters/show.html', {'myth_buster' : myth_buster})

def myth_busters_within_category(request):
    if(request.method == 'GET'):
        categories = MythBusterCategory.objects.filter(myth_busters__isnull = False).distinct()
        return render_to_response('core/myth_busters/list_by_category.html', {'categories' : categories})

def myth_buster_within_category_show(request, myth_buster_category_url, myth_buster_url):
    if(request.method == 'GET'):
        myth_buster_category = MythBusterCategory.objects.filter(url__exact = myth_buster_category_url)[0]
        myth_buster = MythBuster.objects.filter(categories__exact = myth_buster_category, url__exact = myth_buster_url)[0]
        return render_to_response('core/myth_busters/show.html', {'myth_buster_category' : myth_buster_category, 'myth_buster' : myth_buster})

""" Nutrition Tip Categories """
def nutrition_tip_categories_list(request):
    if(request.method == 'GET'):
        nutrition_tip_categories = NutritionTipCategory.objects.filter(nutrition_tips__isnull = False).distinct()
        return render_to_response('core/nutrition_tip_categories/list.html', {'nutrition_tip_categories' : nutrition_tip_categories})

""" Nutrition Tips """
def nutrition_tip_show(request, url):
    if(request.method == 'GET'):
        nutrition_tip = NutritionTip.objects.filter(url__exact = url, make_live__exact = True)
        return render_to_response('core/nutrition_tips/show.html', {'nutrition_tip' : nutrition_tip})

def nutrition_tips_within_category(request):
    if(request.method == 'GET'):
        categories = NutritionTipCategory.objects.filter(nutrition_tips__isnull = False).distinct()
        return render_to_response('core/nutrition_tips/list_by_category.html', {'categories' : categories})

def nutrition_tip_within_category_show(request, nutrition_tip_category_url, nutrition_tip_url):
    if(request.method == 'GET'):
        nutrition_tip_category = NutritionTipCategory.objects.filter(url__exact = nutrition_tip_category_url)[0]
        nutrition_tip = NutritionTip.objects.filter(categories__exact = nutrition_tip_category, url__exact = nutrition_tip_url)[0]
        return render_to_response('core/nutrition_tips/show.html', {'nutrition_tip_category' : nutrition_tip_category, 'nutrition_tip' : nutrition_tip})

""" Pages """
def pages_list(request):
    if(request.method == 'GET'):
        pages = Page.objects.filter(make_live__exact = True)
        return render_to_response('core/pages/list.html', {'pages' : pages})
        
def page_show(request, url):
    if(request.method == 'GET'):
        page = Page.objects.filter(url__exact = url, make_live__exact = True)[0]
        return render_to_response('core/pages/show.html', {'page' : page})

""" Product Categories """
def active_product_categories_list(request):
    if(request.method == 'GET'):
        product_categories = ProductCategory.objects.filter(products__isnull = False).distinct()
        return render_to_response('core/product_categories/active_list.html', {'product_categories' : product_categories})
    
def product_categories_list(request):
    if(request.method == 'GET'):
        product_categories = ProductCategory.objects.all()
        athlete_product_categories = ProductCategory.objects.filter(products__isnull = False, products__for_athletes = True).distinct()
        return render_to_response('core/product_categories/list.html', {'product_categories' : product_categories, 'athlete_product_categories' : athlete_product_categories})

def product_category_show(request, product_category_url):
    if(request.method == 'GET'):
        product_category = ProductCategory.objects.filter(url__exact = product_category_url)[0]
        return render_to_response('core/product_categories/show.html', {'product_category' : product_category})
        
""" Products """
def product_show(request, url):
    if(request.method == 'GET'):
        product = Product.objects.filter(url__exact = url, make_live_exact = True)
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

""" Recipes """
def recipe_show(request, url):
    if(request.method == 'GET'):
        recipe = Recipe.objects.filter(url__exact = url, make_live__exact = True)
        return render_to_response('core/recipes/show.html', {'recipe' : recipe})

def recipes_within_category(request):
    if(request.method == 'GET'):
        categories = RecipeCategory.objects.filter(recipes__isnull = False).distinct()
        return render_to_response('core/recipes/list_by_category.html', {'categories' : categories})

def recipe_within_category_show(request, recipe_category_url, recipe_url):
    if(request.method == 'GET'):
        recipe_category = RecipeCategory.objects.filter(url__exact = recipe_category_url)[0]
        recipe = Recipe.objects.filter(categories__exact = recipe_category, url__exact = recipe_url)[0]
        return render_to_response('core/recipes/show.html', {'recipe_category' : recipe_category, 'recipe' : recipe})

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
        target_model_klass = ContentType.objects.get(model = target_model).model_class()
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

