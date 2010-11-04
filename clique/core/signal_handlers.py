from BeautifulSoup import BeautifulSoup 

# Callback handler to check for orphaned objects.
def orphan_association_check(sender, **kwargs):
    # This is a post_save signal, we have access to sender, instance, and created (True if record was created)
    print sender
    inst = kwargs['instance']
    orphan_fields = inst.orphan_fields()
    
    if len(orphan_fields):
        pass
        # Get all links with "rel=contentassociation".
        
        # Get queryset of contentassociations that match class name and instance id.
        
        # Loop over orphan fields and validate presence of target_model_link_id.
        
        # Delete contentassociation if target_model_link_id fails validation.

# Callback handler to clean up html related to content association.
def clean_association_html(sender, **kwargs):
    print sender
    #print instance.orphan_fields
    
# Callback handler to dispatch common signals.
def common_signal_callback(sender, **kwargs):
    orphan_association_check(sender, **kwargs)
    clean_association_html(sender, **kwargs)
