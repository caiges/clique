import uuid

from BeautifulSoup import BeautifulSoup 

from django.contrib.contenttypes.models import ContentType
from django.db import backend
from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings

from external_apps.categories.models import BaseCategory
from external_apps.contentassociation.models import BaseContentAssociation
from external_apps.pages.models import BasePage
from external_apps.products.models import BaseProduct
from external_apps.recipes.models import BaseRecipe
from external_apps.tags.models import BaseTag

class CategoryPage(BasePage):
    category_description = models.CharField(max_length = 200, blank = True, null = True)
    category_image = models.ImageField(upload_to = 'category_page_images/%Y/%m/%d', blank = True, null = True, default = None)
    remove_category_image = models.BooleanField(blank = True, default = False)
    default_category = models.BooleanField(blank = False, null = False, default = False, help_text = "If checked, this will become the default category.")
    featured = models.BooleanField(blank = True)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    
    class Meta:
        abstract = True
        
class ContentAssociation(BaseContentAssociation):
    target_model_field = models.CharField(max_length = 1000, blank = True, null = True, default = None)
    target_model_link = models.CharField(max_length = 1000, blank = True, null = True, default = None)
    target_model_link_id = models.CharField(max_length = 36, blank = False, null = False, default = uuid.uuid4())   

class Article(BasePage):
    categories = models.ManyToManyField('ArticleCategory', related_name = 'articles', blank = False, null = False)
    featured = models.BooleanField(blank = True)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    include_on_primary_navigation = models.BooleanField(default = False)
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    
    def get_absolute_url(self):
        return '/articles/%s' % self.url
    
    def get_admin_url(self):
        return "/admin/core/article/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
    
    def orphan_fields(self):
        return ['body']
    
class ArticleCategory(CategoryPage):
    
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Article Categories'
        
class Exercise(BasePage):
    categories = models.ManyToManyField('ExerciseCategory', related_name = 'exercises', blank = False, null = False)
    exercise_image = models.ImageField(upload_to = 'exercise_images/%Y/%m/%d', blank = True, null = True, default = None)
    remove_exercise_image = models.BooleanField(blank = True, default = False)
    featured = models.BooleanField(blank = True)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    include_on_primary_navigation = models.BooleanField(default = False)
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    
    def get_absolute_url(self):
        return '/exercises/%s' % self.url
    
    def get_admin_url(self):
        return "/admin/core/exercise/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances

    def orphan_fields(self):
        return ['body']
            
class ExerciseCategory(CategoryPage):
        
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Exercise Categories'

class FitnessTip(BasePage):
    categories = models.ManyToManyField('FitnessTipCategory', related_name = 'fitness_tips', blank = False, null = False)
    featured = models.BooleanField(blank = True)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    include_on_primary_navigation = models.BooleanField(default = False)
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    
    def get_absolute_url(self):
        return '/fitness-tips/%s' % self.url
        
    def get_admin_url(self):
        return "/admin/core/fitnesstip/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances

    def orphan_fields(self):
        return ['body']

class FitnessTipCategory(CategoryPage):
    
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Fitness Tip Categories'

class FunctionalAttribute(BaseTag):
    pass
       
class MythBuster(BasePage):
    categories = models.ManyToManyField('MythBusterCategory', related_name = 'myth_busters', blank = False, null = False)
    featured = models.BooleanField(blank = True)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    include_on_primary_navigation = models.BooleanField(default = False)    
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    
    def get_absolute_url(self):
        return '/myth-busters/%s' % self.url

    def get_admin_url(self):
        return "/admin/core/mythbuster/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances

    def orphan_fields(self):
        return ['body']
            
class MythBusterCategory(CategoryPage):
    
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Myth Buster Categories'

class NutritionalAttribute(BaseTag):
    pass

class NutritionTip(BasePage):
    categories = models.ManyToManyField('NutritionTipCategory', related_name = 'nutrition_tips', blank = False, null = False)
    featured = models.BooleanField(blank = True)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    include_on_primary_navigation = models.BooleanField(default = False)    
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    
    def get_absolute_url(self):
        return '/nutrition-tips/%s' % self.url
    
    def get_admin_url(self):
        return "/admin/core/nutritiontip/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances

    def orphan_fields(self):
        return ['body']
        
class NutritionTipCategory(CategoryPage):
    
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Nutrition Tip Categories'

class Page(BasePage):
    categories = models.ManyToManyField('PageCategory', related_name = 'pages', blank = False, null = False)
    featured = models.BooleanField(blank = True)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    include_on_primary_navigation = models.BooleanField(default = False)    
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    
    def get_absolute_url(self):
        return '/pages/%s' % self.url
    
    def get_admin_url(self):
        return "/admin/core/page/%i" % self.id

    def get_associated_content_items(self):

        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = ContentType.objects.get(app_label = 'core', model = source_model).model_class().objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
 
    def orphan_fields(self):
        return ['body']
        
class PageCategory(CategoryPage):
    
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Page Categories'
    
class Product(BaseProduct):   
    mobile_description = models.TextField(blank = True, null = True, default = None)
    categories = models.ManyToManyField('ProductCategory', related_name = 'products', blank = False, null = False)
    product_image = models.ImageField(upload_to = 'product_images/%Y/%m/%d', blank = True, null = True)
    remove_product_image = models.BooleanField(blank = True, default = False)
    supplement_information_image = models.ImageField(upload_to = 'product_supplement_information_images/%Y/%m/%d', blank = True, null = True)
    remove_supplement_information_image = models.BooleanField(blank = True, default = False)
    for_athletes = models.BooleanField(blank = True, null = False, default = False)
    featured = models.BooleanField(blank = True, null = False, default = False)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    functional_attributes = models.ManyToManyField(FunctionalAttribute, blank = True, null = True)
    nutritional_attributes = models.ManyToManyField(NutritionalAttribute, blank = True, null = True)
    store_link = models.CharField(max_length = 255, blank = True, null = True, default = None)
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    external_url = models.BooleanField(help_text = "Is this product going to point to an external URL?")
    
    def product_categories(self):
        return ', '.join([cat.name for cat in self.categories.all()])
    
    def product_language(self):
        return self.language
    
    def get_absolute_url(self):
        return '/products/%s' % self.url
    
    def get_admin_url(self):
        return '/admin/core/product/%i' % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        source_instances = dict()
        for ca in content_associations:
            # Need array containing field_ids, instance, and link_ids
            instance = ContentType.objects.get(app_label = 'core', model = ca.source_model).model_class().objects.get(pk = ca.source_model_id)
            class_name = instance.__class__.__name__.lower()
            if class_name not in source_instances:
                source_instances[class_name] = dict(field_ids = [], link_ids = [], instance = instance)           
            
            source_instances[class_name].field_ids.append(ca.target_model_field)
            source_instances[class_name].field_ids = list(set(source_instances[class_name].field_ids))
            source_instances[class_name].link_ids.append(ca.target_model_link_id)
            source_instances[class_name].link_ids = list(set(source_instances[class_name].link_ids))
        
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = ContentType.objects.get(app_label = 'core', model = ca.source_model).model_class().objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
        
    def orphan_fields(self):
        return ['long_description', 'product_details', 'mobile_description']
    

class ProductCategory(CategoryPage):
    
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Product Categories'

class Recipe(BaseRecipe):
    categories = models.ManyToManyField('RecipeCategory', related_name = 'recipes', blank = False, null = False)
    also_enjoy = models.ManyToManyField('self', blank = True, null = True)
    featured = models.BooleanField(blank = True)
    sort_order = models.DecimalField(decimal_places = 2, max_digits = 5, blank = True, null = True)
    include_on_primary_navigation = models.BooleanField(default = False)    
    language = models.CharField(max_length = 20, blank = False, null = False, choices = [(lang[0], lang[1]) for lang in settings.LANGUAGES])
    
    def get_absolute_url(self):
        return '/recipes/%s' % self.url
        
    def get_admin_url(self):
        return "/admin/core/recipe/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances

    def orphan_fields(self):
        return ['ingredients', 'directions']
    
class RecipeCategory(CategoryPage):
    
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Recipe Categories'


# Callback handler to check for orphaned objects.
def orphan_association_check(sender, **kwargs):
    # This is a pre_save signal, we have access to sender, instance.
    
    inst = kwargs['instance']
    orphan_fields = inst.orphan_fields()
    
    if len(orphan_fields):
        elements = []
        link_ids = []
        fields = []

        #import rpdb2; rpdb2.start_embedded_debugger("password")
        for f in orphan_fields:

            if str(getattr(inst, f)).strip() != '':
                soup = BeautifulSoup(str(getattr(inst, f)))
                elements = soup.findAll('a', {'rel' : 'contentassociation'})
                        
                for e in elements:
                    link_id = e['id']
                    if link_ids.count("'%s'" % link_id) == 0:
                        # New link.
                        link_ids.append("'%s'" % link_id)                        
                    else:
                        # Duplicate.
                        oa = ContentAssociation.objects.filter(target_model_link_id__exact = link_id)[0]
                        na = ContentAssociation(source_model = oa.source_model, source_model_id = oa.source_model_id, target_model = oa.target_model, target_model_id = oa.target_model_id, target_model_field = oa.target_model_field, target_model_link = oa.target_model_link, target_model_link_id = uuid.uuid4())
                        na.save()
                        e['id'] = na.target_model_link_id
                        link_ids.extend(["'%s'" % na.target_model_link_id])
                setattr(inst, f, str(soup))

    
                fields.append(f)
            
        # Remove duplicates.
        link_ids = list(set(link_ids))
        #print link_ids
        if len(link_ids):
            orphan_content_associations = ContentAssociation.objects.raw("select * from core_contentassociation where (source_model = '%s' and source_model_id = '%i' and target_model_link_id not in (%s))" % (inst.__class__.__name__.lower(), inst.id, ','.join(link_ids)))
            for oca in orphan_content_associations:
                oca.delete()
        elif inst.id != None:
            orphan_content_associations = ContentAssociation.objects.raw("select * from core_contentassociation where (source_model = '%s' and source_model_id = '%i')" % (inst.__class__.__name__.lower(), inst.id))
            for oca in orphan_content_associations:
                oca.delete()
        
# Callback handler to clean up html related to content association.
def clean_association_html(sender, **kwargs):
    print sender
    #print instance.orphan_fields
    
# Callback handler to dispatch common signals.
def common_signal_callback(sender, **kwargs):
    orphan_association_check(sender, **kwargs)
    #clean_association_html(sender, **kwargs)


# Register models with the orphan association check callback.
#pre_save.connect(common_signal_callback, sender = Article)
#pre_save.connect(common_signal_callback, sender = Exercise)    
#pre_save.connect(common_signal_callback, sender = FitnessTip)
#pre_save.connect(common_signal_callback, sender = MythBuster)    
#pre_save.connect(common_signal_callback, sender = NutritionTip)
#pre_save.connect(common_signal_callback, sender = Page)
pre_save.connect(orphan_association_check, sender = Product, dispatch_uid = uuid.uuid4())
#pre_save.connect(common_signal_callback, sender = Recipe)
