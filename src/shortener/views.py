from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import KirrURL

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.POST['url'])
        print(request.POST.get('url'))
        return render(request, "shortener/home.html", {}) 

def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
    #PAGE NOT FOUNT
    obj = get_object_or_404(KirrURL, shortcode=shortcode)#yello is field name, white is passed arg
    return HttpResponseRedirect(obj.url)

class KirrCBView(View): #class based views, must specify method
    def get(self, request, shortcode=None, *args, **kwargs):

        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)




"""
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view


    #PAGE NOT FOUNT
    obj = get_object_or_404(KirrURL, shortcode=shortcode)#yello is field name, white is passed arg
    obj_url = obj.url

    RAISES EXCEPTION IS INPUT SHORTCODE DOESN'T EXIST
    try:
        obj = KirrURL.objects.get(shortcode=shortcode)
    except:
        obj = KirrURL.objects.all().first()
    try/except handles all exceptions in the same way

    ANOTHER WAY TO HANDLE NON-EXISTANT SHORTCODE
    obj_url = None
    #query set is created only if input shortcode matches stored shortcode exactly
    qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    #if qs (shortcode) even exists, and count is 1 (all should be unique)
    if qs.exists() and qs.count() == 1:
        #then grab the first from the query set
        obj = qs.first()
        obj_url = obj.url

    return HttpResponse("hello {sc}".format(sc=obj_url))

"""
