from django.core.signals import request_started

def set_default_language(sender, **kwargs):
    r = kwargs
    print sender
    #if 'django_language' not in r.session:
    #        r.session['django_language'] = 'en'
    
    
    
# Connect the request_started signal.
request_started.connect(set_default_language)