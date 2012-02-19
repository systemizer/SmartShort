import json
import hashlib
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.template import RequestContext

from django.conf import settings

from smartshort.main.models import URL

'''
If the user doesnt have the extension, then this 
will be called
'''        
def get(request):
    return render_to_response("get_extension.html",{},RequestContext(request))        



'''
Takes in a post request from the extension that has 
url parameters url,shared,and scrolled. This should only
be called by the extension
'''
def extension_create(request):
    if not request.method=="POST":
        raise Http404

    url = request.POST.get("url")
    shared = request.POST.get("shared")
    scrolled = request.POST.get("scrolled")        
    
    url = URL(url=url,shared=shared,scrolled=scrolled)
    url.save()
    url.shared_url = "%s/?id=%s" % (settings.DOMAIN,url.id)
    url.save()
    return HttpResponse(json.dumps({'url':url.shared_url},mimetype="application/json"))


'''
If the user DOES have the extension, then we will give the extension some json
'''
def extension_get(request):
    id = request.GET.get("id")
    if not id:
        return HttpResponseBadRequest("ID not found")
    try:
        url = URL.objects.get(id=id)
        context = {'id':id,
                   'shared_domain':url.shared_domain,
                   'shared_url':url.shared_domain,
                   'shared':url.shared,
                   'scrolled':url.scrolled,
                   }
        return HttpResponse(json.dumps(context),mimetype="application/json")
    except URL.DoesNotExist:
        return HttpResponseBadRequest(json.dumps({'error':'not found'}),mimetype="application/json")
        

