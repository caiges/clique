import uuid

from BeautifulSoup import BeautifulSoup 

from django.db import backend
from django.db import models
from django.db.models.signals import pre_save

from multilingual.translation import TranslationModel

from external_apps.categories.models import BaseCategory
from external_apps.contentassociation.models import BaseContentAssociation
from external_apps.pages.models import BasePage
from external_apps.products.models import BaseProduct
from external_apps.recipes.models import BaseRecipe
from external_apps.tags.models import BaseTag

class CategoryPage(BasePage):
    category_description = models.CharField(max_length = 200, blank = True, null = True)
    category_image = models.ImageField(upload_to = 'category_page_images/%Y/%m/%d', blank = True, null = True, default = None)
    default_category = models.BooleanField(blank = False, null = False, default = False, help_text = "If checked, this will become the default category.")
    
    class Meta:
        abstract = True
        
class ContentAssociation(BaseContentAssociation):
    target_model_field = models.CharField(max_length = 1000, blank = True, null = True, default = None)
    target_model_link = models.CharField(max_length = 1000, blank = True, null = True, default = None)
    target_model_link_id = models.CharField(max_length = 36, blank = False, null = False, default = uuid.uuid4())   

class Article(BasePage):
    category = models.ManyToManyField('ArticleCategory', related_name = 'article_categories', blank = False, null = False)

    @models.permalink
    def get_absolute_url(self):
        return ('article_show', [str(self.id)])
    
    def get_admin_url(self):
        return "/admin/core/article/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        
        # Argument a is an instance of ContentAssociation
        """def flatten_associations(a, ca_list):
            for ca in ca_list:
                if a.source_model == ca.source_model and a.source_model_id = ca.source_model_id and a.target_model = ca.target_model and a.target_model_id = ca.target_model_id
                    ca.append(dict(instance))
        """
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
    
class ArticleCategory(CategoryPage):

    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Article Categories'
        
class Exercise(BasePage):
    category = models.ManyToManyField('ExerciseCategory', related_name = 'exercise_categories', blank = False, null = False)

    @models.permalink
    def get_absolute_url(self):
        return ('exercise_show', [str(self.id)])
    
    def get_admin_url(self):
        return "/admin/core/exercise/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        
        # Argument a is an instance of ContentAssociation
        """def flatten_associations(a, ca_list):
            for ca in ca_list:
                if a.source_model == ca.source_model and a.source_model_id = ca.source_model_id and a.target_model = ca.target_model and a.target_model_id = ca.target_model_id
                    ca.append(dict(instance))
        """
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
        
class ExerciseCategory(CategoryPage):

    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Exercise Categories'

class FitnessTip(BasePage):
    category = models.ManyToManyField('FitnessTipCategory', related_name = 'fitness_tip_categories', blank = False, null = False)

    @models.permalink
    def get_absolute_url(self):
        return ('fitness_tip_show', [str(self.id)])
        
    def get_admin_url(self):
        return "/admin/core/fitnesstip/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        
        # Argument a is an instance of ContentAssociation
        """def flatten_associations(a, ca_list):
            for ca in ca_list:
                if a.source_model == ca.source_model and a.source_model_id = ca.source_model_id and a.target_model = ca.target_model and a.target_model_id = ca.target_model_id
                    ca.append(dict(instance))
        """
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances

class FitnessTipCategory(CategoryPage):

    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Fitness Tip Categories'

class FunctionalAttribute(BaseTag):
    pass
       
class MythBuster(BasePage):
    category = models.ManyToManyField('MythBusterCategory', related_name = 'myth_buster_categories', blank = False, null = False)

    @models.permalink
    def get_absolute_url(self):
        return ('myth_buster_show', [str(self.id)])

    def get_admin_url(self):
        return "/admin/core/mythbuster/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        
        # Argument a is an instance of ContentAssociation
        """def flatten_associations(a, ca_list):
            for ca in ca_list:
                if a.source_model == ca.source_model and a.source_model_id = ca.source_model_id and a.target_model = ca.target_model and a.target_model_id = ca.target_model_id
                    ca.append(dict(instance))
        """
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
        
class MythBusterCategory(CategoryPage):

    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Myth Buster Categories'

class NutritionalAttribute(BaseTag):
    pass

class NutritionTip(BasePage):
    category = models.ManyToManyField('NutritionTipCategory', related_name = 'nutrition_tip_categories', blank = False, null = False)

    @models.permalink
    def get_absolute_url(self):
        return ('nutrition_tip_show', [str(self.id)])
    
    def get_admin_url(self):
        return "/admin/core/nutritiontip/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        
        # Argument a is an instance of ContentAssociation
        """def flatten_associations(a, ca_list):
            for ca in ca_list:
                if a.source_model == ca.source_model and a.source_model_id = ca.source_model_id and a.target_model = ca.target_model and a.target_model_id = ca.target_model_id
                    ca.append(dict(instance))
        """
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
        
class NutritionTipCategory(CategoryPage):

    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Nutrition Tip Categories'

class Page(BasePage):
    category = models.ManyToManyField('PageCategory', related_name = 'page_categories', blank = False, null = False)

    @models.permalink
    def get_absolute_url(self):
        return ('page_show', [str(self.id)])
    
    def get_admin_url(self):
        return "/admin/core/page/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        
        # Argument a is an instance of ContentAssociation
        """def flatten_associations(a, ca_list):
            for ca in ca_list:
                if a.source_model == ca.source_model and a.source_model_id = ca.source_model_id and a.target_model = ca.target_model and a.target_model_id = ca.target_model_id
                    ca.append(dict(instance))
        """
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
        
class PageCategory(CategoryPage):
        
    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Page Categories'
    
class Product(BaseProduct):
    category = models.ManyToManyField('ProductCategory', related_name = 'product_categories', blank = False, null = False)
    product_image = models.ImageField(upload_to = 'product_images/%Y/%m/%d', blank = True)
    supplement_information_image = models.ImageField(upload_to = 'product_supplement_information_images/%Y/%m/%d', blank = True)
    for_athletes = models.BooleanField(blank = True, null = False, default = False)
    featured = models.BooleanField(blank = True, null = False, default = False)
    functional_attributes = models.ManyToManyField(FunctionalAttribute, blank = True, null = True)
    nutritional_attributes = models.ManyToManyField(NutritionalAttribute, blank = True, null = True)
    
    class Translation(TranslationModel):
        name = models.CharField(max_length = 100, blank = False, null = False)
        page_title = models.CharField(max_length = 200, blank = False, null = False)
        url = models.CharField(max_length = 1000, blank = False, null = False, help_text = "URL will be appended to /products/...")
        meta_description = models.CharField(max_length = 500, blank = True, null = True)
        meta_keywords = models.CharField(max_length = 500, blank = True, null = True, default = None, help_text = 'Format: (keyword-one, keyword-two)')
        long_description = models.TextField(blank = True, null = True, default = None)
        product_details = models.TextField(blank = True, null = True, default = None)
        store_link = models.CharField(max_length = 255, blank = True, null = True, default = None)
        mobile_long_description = models.TextField(blank = True, null = True, default = None)
    
    @models.permalink
    def get_absolute_url(self):
        return ('product_show', [str(self.id)])
    
    def get_admin_url(self):
        return "/admin/core/product/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        
        # Argument a is an instance of ContentAssociation
        """def flatten_associations(a, ca_list):
            for ca in ca_list:
                if a.source_model == ca.source_model and a.source_model_id = ca.source_model_id and a.target_model = ca.target_model and a.target_model_id = ca.target_model_id
                    ca.append(dict(instance))
        """
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
        
    def orphan_fields(self):
        return ['long_description', 'product_details', 'mobile_long_description']

class ProductCategory(CategoryPage):

    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Product Categories'

class Recipe(BaseRecipe):
    category = models.ManyToManyField('RecipeCategory', related_name = 'recipe_categories', blank = False, null = False)
    also_enjoy = models.ManyToManyField('self', blank = True, null = True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('recipe_show', [str(self.id)])
        
    def get_admin_url(self):
        return "/admin/core/recipe/%i" % self.id

    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(target_model__exact = self.__class__.__name__.lower(), target_model_id = self.id)
        
        # Argument a is an instance of ContentAssociation
        """def flatten_associations(a, ca_list):
            for ca in ca_list:
                if a.source_model == ca.source_model and a.source_model_id = ca.source_model_id and a.target_model = ca.target_model and a.target_model_id = ca.target_model_id
                    ca.append(dict(instance))
        """
        content_association_source_instances = [dict(field_ids = ','.join(list(set([cai.target_model_field for cai in content_associations]))), instance = globals()[ca.source_model.capitalize()].objects.get(pk = ca.source_model_id), link_ids = ','.join([cal.target_model_link_id for cal in content_associations])) for ca in content_associations]
        return content_association_source_instances
    
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
