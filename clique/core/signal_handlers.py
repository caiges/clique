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
        for f in orphan_fields:
            soup = BeautifulSoup(getattr(inst, f))
            
            if len(elements) == 0:
                elements = soup.findAll('a', {'rel' : 'contentassociation'})
            else:
                elements.extend(soup.findAll('a', {'rel' : 'contentassociation'}))
                
            if len(link_ids) == 0:
                link_ids = ["'%s'" % e['id'] for e in elements]
            else:
                link_ids.extend(["'%s'" % e['id'] for e in elements])
        print 'trace'
        #print link_ids        
        # Remove duplicates.
        link_ids = list(set(link_ids))
        #print link_ids
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
