import uuid

from BeautifulSoup import BeautifulSoup 

# Callback handler to check for orphaned objects.
def orphan_association_check(sender, **kwargs):
    # This is a pre_save signal, we have access to sender, instance.
    
    from django.db import backend

    from models import *

    inst = kwargs['instance']
    orphan_fields = inst.orphan_fields()
    
    if len(orphan_fields):
        elements = []
        link_ids = []
        fields = []
        
        for f in orphan_fields:
            if getattr(inst, f).strip() != '':
                soup = BeautifulSoup(getattr(inst, f))
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

                #setattr(inst, f, soup)

    
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
