__author__ = 'Nir'
import yql


def getNumbeoData(country, city):

    #Define the URL to query in the Numbeo web page (by country and city)
    URL = "http://www.numbeo.com/cost-of-living/city_result.jsp?country=" + country + "&city=" + city + "&displayCurrency=ILS"

    #Fix the + problem
    URL = URL.replace(' ', "+")

    #Create an object that will handle the communication with Yahoo!'s YQL
    y = yql.Public()

    #Define the SQL query that will be used in YQL. This will return us the price of 1 pair of Nike Shoes.
    query = "select * from html where url='" + URL + "' and xpath='//p[text()=\"1 Pair of Nike Shoes\"]/../following-sibling::td[1]/p'"

    #Preform the query and return the results to the object result
    result = y.execute(query)

    #get the rows of the result (in our case, just 1) and give to rows
    rows = result.rows

    #return the only row.
    return rows[0]
