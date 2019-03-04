import scrapy
import json

class LinksCyT(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
        	'https://www.casasyterrenos.com/inmobiliaria.neximo/1'
		]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sites = response.css('#resultados > div > div > div.col-md-4.img-resultado > a::attr(href)').getall()
        urls_sites = dict()
        urls_sites['sites'] = sites
        with open("sites_cyt.json", 'w') as f:
            json.dump(urls_sites, f)
