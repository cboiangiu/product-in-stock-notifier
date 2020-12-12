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
        # check if product is in stock
        if self.page.find("div", {"class": "product-container"}).find("span", {"class": "available"}) != None:
            return True
        # check if product is not in stock
        elif self.page.find("div", {"class": "product-container"}).find("span", {"class": "not-available"}) != None:
            return False
        # if neither assume page css has changed and the class needs to be updated
        return None

    def is_page_valid(self):
        # verify that we are on a valid product page by checking
        # that we have our container div for the product
        # 
        # some stores give you a captcha or display a warning page
        # after too many request, so we detect that and change ip
        if self.page.find("div", {"class": "product-container"}) != None:
            return True
        return False
