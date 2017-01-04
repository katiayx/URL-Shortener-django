from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
    #
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()

    #better
    qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()

    return HttpResponse("hello {sc}".format(sc=shortcode))

class KirrCBView(View): #class based views
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("hello again {sc}".format(sc=shortcode))
