import threading

import requests
from bs4 import BeautifulSoup

class WikiWorker():
    def __init__(self):
        self._url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    @staticmethod
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html)
        table = soup.find(id='constituents')
        table_rows = table.find_all('tr')
        for table_row in table_rows:
            symbol_td = table_row.find('td')
            if symbol_td:
                symbol_a = symbol_td.find('a')
                if symbol_a:
                    symbol = symbol_a.text
                    yield symbol

    def get_sp_500_companies(self):
        response = requests.get(url=self._url)
        if response.status_code!= 200:
            print("Couldn't get entries")
            return []
        yield from self._extract_company_symbols(response.text)

if __name__ =="__main__":
    wiki_worker = WikiWorker()
    symbol_list = []

    for symbol in wiki_worker.get_sp_500_companies():
        symbol_list.append(symbol)

    print(symbol_list)