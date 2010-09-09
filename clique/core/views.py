from django.shortcuts import render_to_response

def index(request):
    if(request.method == 'GET'):
        return render_to_response('core/index.html')
        
def association_test(request):
    if(request.method == 'GET'):
        return render_to_response('core/association-test.html')