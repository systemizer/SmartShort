import json
import hashlib
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from smartshort.main.decorators import AllowJSONPCallback
from smartshort.main.models import URL

'''
If the user doesnt have the extension, then this 
will be called
'''        
def get(request):
    return render_to_response("get_extension.html",{},RequestContext(request))        
def how_it_works(request):
    return render_to_response("how-it-works.html",{},RequestContext(request))


'''
Takes in a get request from the extension that has 
url parameters url,shared,and scrolled. This should only
be called by the extension
'''
@csrf_exempt
@AllowJSONPCallback
def extension_create(request):
    url = request.GET.get("url")
    shared = request.GET.get("shared")
    scrolled = request.GET.get("scrolled")        
    
    url = URL(url=url,shared=shared,scrolled=scrolled)
    url.save()
    url.shared_url = "%s/?id=%s" % (settings.DOMAIN,url.id)
    url.save()
    return HttpResponse(json.dumps({'url':url.shared_url}),content_type="application/json")


'''
If the user DOES have the extension, then we will give the extension some json
'''
@AllowJSONPCallback
def extension_get(request):
    id = request.GET.get("id")
    if not id:
        return HttpResponseBadRequest("ID not found")
    try:
        url = URL.objects.get(id=id)
        context = {'id':id,
                   'url':url.url,
                   'shared':url.shared,
                   'scrolled':url.scrolled,
                   }
        return HttpResponse(json.dumps(context),content_type="application/json")
    except URL.DoesNotExist:
        return HttpResponseBadRequest(json.dumps({'error':'not found'}),content_type="application/json")
        

