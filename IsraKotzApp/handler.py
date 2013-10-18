from django.shortcuts import render_to_response
from django.template import RequestContext
from piston.handler import BaseHandler
from IsraKotzApp.collectNumbeoData import getNumbeoData
from IsraKotzApp.models import City, Product

__author__ = 'Nir'
class BudgetHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = City

    def read(self, request,city):
            city = city.replace("+", " ")
            try:
                result = City.objects.get(city=city)
                product_prices = Product.objects.all()
                products = {}
                products["city"] = city
                for product in product_prices:
                    price_value = getNumbeoData(result.country,city, product.code)
                    products[product.name] = {"name":product.code,"price": price_value}
            except BaseException:
                return render_to_response("404.html", {"city": city},context_instance=RequestContext(request))
            return render_to_response("Budget.html",{"product":products}, context_instance=RequestContext(request))