# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from IsraKotzApp.collectNumbeoData import getNumbeoData


def home(Request):
    price_value = getNumbeoData("Israel","Tel Aviv-Yafo")
    products = {"name": "1 Pair of Nike Shoes", "price": price_value}
    return render_to_response("Home.html",products, context_instance=RequestContext(Request))