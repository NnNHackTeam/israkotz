# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from IsraKotzApp.collectNumbeoData import getNumbeoData
from IsraKotzApp.models import City


def home(Request):
    return render_to_response("Home.html", context_instance=RequestContext(Request))

def budget(Request):
    if Request.is_ajax():
        city = Request.POST['city']
        result = City.objects.get(city=city)
        price_value = getNumbeoData(result.country,city)
        products = {"name": "1 Pair of Nike Shoes", "price": price_value}
        return render_to_response("Budget.html",products, context_instance=RequestContext(Request))