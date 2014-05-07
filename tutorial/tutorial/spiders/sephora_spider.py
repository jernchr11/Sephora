from scrapy.spider import Spider
from scrapy.selector import Selector
import json

from tutorial.items import SephoraItem

class SephoraSpider(Spider):
    name = "sephora"
    allowed_domains = ["http://www.sephora.com"]
    base_url = "http://www.sephora.com/"
    sort_query = "?defaultSortBy=-1&pageSize=-1"
    components = ["foundation-sets","foundation-makeup","tinted-moisturizer","bb-cc-cream-face-makeup","makeup-primer-face-primer","setting-powder-face-powder","concealer","blush-face-makeup","bronzer-makeup","luminizer-luminous-makeup","blotting-paper-oil-control","makeup-remover","sponges-applicators-makeup-brushes-applicators-makeup","face-brushes-makeup-brushes-applicators-makeup","eyeshadow-palettes","mascara-eyes-makeup","eyeliner","eyeshadow","eyeshadow-primer-eye-primer","under-eye-concealer","eyebrow-makeup-pencils","eyelash-enhancers-eyelash-primer","eyelash-curlers-eyes-makeup","fake-eyelashes-false-eyelashes","eye-makeup-remover","eye-brushes-makeup-brushes-applicators-makeup","lip-palettes-lipstick-palettes","lipstick","lip-plumper","lip-stain","lip-liner-lip-pencils","lip-balm-treatments-lips-makeup","lip-brushes-makeup-brushes-applicators-makeup","makeup-palettes","makeup-value-sets","brush-sets-makeup-brushes-applicators-makeup"]
    #components = ["foundation-sets"]

    start_urls = [base_url + component + sort_query for component in components];



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
