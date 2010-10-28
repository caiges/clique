from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *
    
def admin_conflicts_show(request):
    return render_to_response('admin/conflicts.html', {'content_assications' : content_assications})
