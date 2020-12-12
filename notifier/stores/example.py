# This file is not used!
# This just showcases how you might create a class
# for the store of the product you want to get notified 
# when it is in stock.
# 
# After you create the class, make sure to import 
# and add it to the products list in ../products.py
from modules.store import Store

class Example(Store):
    def __init__(self, product, url):
        super().__init__(product, "Example Store", url)

    def is_in_stock(self):
        if self.page.find("div", {"class": "product-container"}).find("span", {"class": "available"}) != None:
            return True
        return False

    def is_page_valid(self):
        if self.page.find("div", {"class": "product-container"}) != None:
            return True
        return False
