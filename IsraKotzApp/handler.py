from django.shortcuts import render_to_response
from django.template import RequestContext
from piston.handler import BaseHandler
from IsraKotzApp.HotelSearcher import getHotelData
from IsraKotzApp.collectNumbeoData import getNumbeoData
from IsraKotzApp.models import City, Product

__author__ = 'Nir'
class BudgetHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = City

    def read(self, request,city):
            city = city.replace("+", " ")
            result = ""
            try:
                result = City.objects.get(city=city)
            except BaseException:
                return render_to_response("404.html", {"city": city},context_instance=RequestContext(request))
            try:
                calc = 0
                product_prices = Product.objects.all()
                products = {}
                products["city"] = city
                products["country"] = result.country
                for product in product_prices:
                    price_value = getNumbeoData(result.country,city, product.code)
                    ?calc = calc + float(price_value[0:-2])
                    products[product.name] = {"name":product.code,"price": price_value}
                hotel_prices = getHotelData(result.country, city)
                #calc = calc + float(hotel_prices["five_star"]["price"][0:-2])
                #products["calc"] = calc
                products["hotels"] = hotel_prices
            except BaseException:
                return render_to_response("general.html",context_instance=RequestContext(request))
            return render_to_response("Budget.html",{"product":products}, context_instance=RequestContext(request))