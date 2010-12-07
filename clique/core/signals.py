from django.contrib.sessions.backends.db import SessionStore
from django.core.signals import request_started

def set_default_language(sender, **kwargs):
    r = kwargs
    print '---------- TRACE --------'
    print sender.request_class
    #print sender.request_class.REQUEST
    #print r
    #if 'django_language' not in r.session:
    #        r.session['django_language'] = 'en'
    
    
    
# Connect the request_started signal.
request_started.connect(set_default_language)