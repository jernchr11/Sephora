from scrapy.spider import Spider
from scrapy.selector import Selector
import json

from tutorial.items import SephoraItem

class SephoraSpider(Spider):
    name = "sephora"
    allowed_domains = ["http://www.sephora.com"]
    start_urls = [
        "http://www.sephora.com/makeup-primer-face-primer?defaultSortBy=-1&pageSize=-1", "http://www.sephora.com/foundation-makeup?defaultSortBy=-1&pageSize=-1",
        "http://www.sephora.com/bb-cc-cream-face-makeup?defaultSortBy=-1&pageSize=-1", "http://www.sephora.com/foundation-sets?defaultSortBy=-1&pageSize=-1",
        "http://www.sephora.com/setting-powder-face-powder?defaultSortBy=-1&pageSize=-1", "http://www.sephora.com/concealer?defaultSortBy=-1&pageSize=-1",
        "http://www.sephora.com/blush-face-makeup?defaultSortBy=-1&pageSize=-1", "http://www.sephora.com/bronzer-makeup?defaultSortBy=-1&pageSize=-1",
        "http://www.sephora.com/luminizer-luminous-makeup?defaultSortBy=-1&pageSize=-1", "http://www.sephora.com/face-brushes-makeup-brushes-applicators-makeup?defaultSortBy=-1&pageSize=-1"
    ]

    def parse(self, response):
        sel = Selector(response)
        products = json.loads("{"+sel.re("\"products\":\[.*\]")[0]+"}")
        items = []
        for product in products["products"]:
            #print(product)
            item = SephoraItem()
            item['display_name'] = product["display_name"]
            item['list_price'] = product["derived_sku"]["list_price"]
            item['brand_name'] = product["brand_name"]
            item['rating'] = product["rating"]
            items.append(item)
        return items
