from abc import ABC
import requests
from bs4 import BeautifulSoup
from random_proxies import random_proxy
from modules.product_status import Status

class Store(ABC):
    should_notify_page_changed = True

    def __init__(self, product, store, url):
        self.product = product
        self.store = store
        self.url = url
        self.should_notify = True

    def check(self, user_agent, proxy_country_code):
        try:
            self.get_page_data(user_agent, proxy_country_code)
            if not self.is_page_valid():
                return Status.FAIL
            in_stock = self.is_in_stock()
            if in_stock == None and Store.should_notify_page_changed:
                Store.should_notify_page_changed = False
                return Status.PAGE_CHANGED_SHOULD_NOTIFY
            elif in_stock == None:
                return Status.PAGE_CHANGED
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

    def get_page_data(self, user_agent, proxy_country_code):
        proxy = random_proxy(code=proxy_country_code)
        headers = {'User-Agent': user_agent}
        response = requests.get(self.url, headers = headers, timeout=5, proxies={"http":"http://"+proxy})
        if response is None or response.status_code != 200:
            raise Exception('Request failed for ' + self.url)
        content = response.text
        self.page = BeautifulSoup(content, "html.parser")

    def is_in_stock():
        pass

    def is_page_valid():
        pass
