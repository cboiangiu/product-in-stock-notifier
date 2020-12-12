from abc import ABC
import requests
from bs4 import BeautifulSoup
from modules.product_status import Status

class Store(ABC):
    def __init__(self, product, store, url):
        self.product = product
        self.store = store
        self.url = url
        self.should_notify = True

    def check(self, user_agent):
        try:
            self.get_page_data(user_agent)
            if not self.is_page_valid():
                return Status.FAIL
            in_stock = self.is_in_stock()
            if in_stock and self.should_notify:
                self.should_notify = False
                return Status.NOTIFY_STOCK
            elif not in_stock:
                self.should_notify = True
        except:
            return Status.FAIL
        return Status.NOTHING

    def get_product(self):
        return self.product

    def get_store(self):
        return self.store

    def get_url(self):
        return self.url

    def get_page_data(self, user_agent):
        headers = {'User-Agent': user_agent}
        response = requests.get(self.url, headers = headers, timeout=5)
        if response is None or response.status_code != 200:
            raise Exception('Request failed for ' + self.url)
        content = response.text
        self.page = BeautifulSoup(content, "html.parser")

    def is_in_stock():
        pass

    def is_page_valid():
        pass