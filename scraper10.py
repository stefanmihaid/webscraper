from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen


#read the HTML and parse it
def parse_autovit(url):
    request = Request(url, headers={'User-Agent' : "Google Chrome"})
    content =urlopen(request).read()
    soup_html = soup(content, "html.parser")
    return soup_html

def get_toppage(url):
    no = []
    autovit = parse_autovit(url)
    pages = autovit.findAll("span", {"class": "page"})
    for page in pages:
        no.append(page.text)
    return no[len(no)-2]

def get_cars(url):
    soup_html = parse_autovit(url)
    offers = soup_html.find("div", {"class": "offers list"})
    oferte = offers.findAll('article')
    for offer in oferte:
        try:
            car_model = offer.find("div", {"class": "offer-item__title"}).h2.a["title"]
            car_price = offer.find("div", {"class": "offer-item__price"}).find("span", "offer-price__number").text.replace("                    ", " ")
            car_year = offer.find("li", {"data-code": "year"}).span.text
            car_km = offer.find("li", {"data-code": "mileage"}).span.text
            car_cmc = offer.find("li", {"data-code": "engine_capacity"}).span.text
            car_gas = offer.find("li", {"data-code": "fuel_type"}).span.text
            car_url = offer.find("div", {"class": "offer-item__photo"}).a['href']
            print (car_url)
            print (car_year)
        except Exception:
            pass



def go_trrough_all_pages():
    base_link = "https://www.autovit.ro/autoturisme"
    page_link = "?search%5Bcountry%5D=&page="
    model = "a4"
    make = "audi"
    first_link = base_link+"/"+make+"/"+model
    max_page_count = int(get_toppage(first_link))
    for i in range(0,max_page_count):
        url = (base_link+"/"+make+"/"+model+"/"+page_link+str(i+1))
        print (url)
        get_cars(url)


go_trrough_all_pages()
