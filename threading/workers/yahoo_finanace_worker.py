import threading
import requests
from lxml import html
import time
import random


class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        self._input_queue = input_queue
        super(YahooFinancePriceScheduler, self).__init__(**kwargs)
        self.start()

    def run(self):
        while True:
            val = self._input_queue.get()
            if val=='DONE':
                break
            yahoo_worker = YahooFinancePriceWorker(val)
            price = yahoo_worker.get_price()
            print(f"Price for symbol {val}: {price}")
            time.sleep(random.random())


# class YahooFinancePriceWorker(threading.Thread):
class YahooFinancePriceWorker:
    def __init__(self, symbol, **kwargs):
        self._symbol = symbol
        super(YahooFinancePriceWorker, self).__init__(**kwargs)
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f"{base_url}{symbol}/"
        # self.start()

    def run(self):
        time.sleep(30*random.random())
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        r = requests.get(self._url, headers=headers)
        print(f"Status code for symbol {self._symbol}: {r.status_code}")
        if r.status_code != 200:
            return
        tree = html.fromstring(r.content)
        price = float(tree.xpath('/html/body/div[2]/main/section/section/section/article/section[1]/div[2]/div[1]/section/div/section[1]/div[1]/div[1]/span')[0].text.replace(",", "").strip())
        print(f"Price for symbol {self._symbol}: {price}")

    def get_price(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        r = requests.get(self._url, headers=headers)
        print(f"Status code for symbol {self._symbol}: {r.status_code}")
        if r.status_code != 200:
            return
        tree = html.fromstring(r.content)
        price = float(tree.xpath('/html/body/div[2]/main/section/section/section/article/section[1]/div[2]/div[1]/section/div/section[1]/div[1]/div[1]/span')[0].text.replace(",", "").strip())
        return price

if __name__ == "__main__":
    yahoo_worker = YahooFinancePriceWorker("COF")