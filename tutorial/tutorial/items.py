from scrapy.item import Item, Field

class SephoraItem(Item):
    rating = Field()
    display_name = Field()
    brand_name = Field()
    list_price = Field()
