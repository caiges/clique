import uuid

from django.db import models
from django.db.models.signals import post_save
from external_apps.categories.models import BaseCategory
from external_apps.contentassociation.models import BaseContentAssociation
from external_apps.pages.models import BasePage
from external_apps.products.models import BaseProduct
from external_apps.recipes.models import BaseRecipe

class CategoryPage(BasePage):
    category_description = models.CharField(max_length = 200, blank = True, null = True)
    category_image = models.ImageField(upload_to = 'category_page_images/%Y/%m/%d', blank = True, null = True, default = None)
    default_category_page = models.BooleanField(blank = False, null = False, default = False, help_text = "If checked, this will become the category index page.")
    
    class Meta:
        abstract = True
        
class ContentAssociation(BaseContentAssociation):
    target_model_field = models.CharField(max_length = 1000, blank = True, null = True, default = None)
    target_model_link = models.CharField(max_length = 1000, blank = True, null = True, default = None)
    target_model_link_id = models.CharField(max_length = 36, blank = False, null = False, default = uuid.uuid4())
    
    def orphan_association_check(sender, **kwargs):
        # This is a post_save signal, we have access to sender, instance, and created (True if record was created)
        
        print sender
        
        # Loop through all sender associations.
        
        # Parse the target_model_field for target_model_link_id.
        
        # If target_model_link_id is not present, delete the association.
        
    post_save.connect(orphan_association_check)

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
    product_image = models.ImageField(upload_to = 'product_images/%Y/%m/%d')
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

class ProductCategory(CategoryPage):

    class Meta(CategoryPage.Meta):
        verbose_name_plural = 'Product Categories'

class Recipe(BaseRecipe):
    category = models.ManyToManyField('RecipeCategory', related_name = 'recipe_categories', blank = False, null = False)
    
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
