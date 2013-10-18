# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from IsraKotzApp.collectNumbeoData import getNumbeoData
from IsraKotzApp.models import City


def home(Request):
    return render_to_response("Home.html", context_instance=RequestContext(Request))

def autocomplete_city(request):
    term = request.GET.get('term') #jquery-ui.autocomplete parameter
    cities = City.objects.filter(city__istartswith=term) #lookup for a city
    res = []
    for c in cities:
         #make dict with the metadatas that jquery-ui.autocomple needs (the documentation is your friend)
         dict = {'id':c.id, 'label':c.city, 'value':c.city}
         res.append(dict)
    return HttpResponse(simplejson.dumps(res))