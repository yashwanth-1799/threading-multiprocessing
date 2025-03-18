import time
from multiprocessing import Queue

from workers.wiki_worker import WikiWorker
from workers.yahoo_finanace_worker import YahooFinancePriceWorker, YahooFinancePriceScheduler

def main():
    scraper_start_time = time.time()
    wiki_worker = WikiWorker()
    current_workers = []
    for symbol in wiki_worker.get_sp_500_companies():
        yahoo_worker = YahooFinancePriceWorker(symbol)
        current_workers.append(yahoo_worker)

    for worker in current_workers:
        worker.join()

    print(f"Time for Extracting content: {round(time.time()- scraper_start_time, 1)}")


def queue_main():
    scraper_start_time = time.time()
    symbol_queue = Queue()
    wiki_worker = WikiWorker()
    yahoo_finance_price_scheduler_threads = []
    num_yahoo_finance_price_worker = 4
    for  i in range(num_yahoo_finance_price_worker):
        scheduler = YahooFinancePriceScheduler(input_queue=symbol_queue)
        yahoo_finance_price_scheduler_threads.append(scheduler)

    for symbol in wiki_worker.get_sp_500_companies():
        symbol_queue.put(symbol)

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put("DONE")

    for worker in yahoo_finance_price_scheduler_threads:
        worker.join()

    print(f"Time for Extracting content: {round(time.time()- scraper_start_time, 1)}")

if __name__ == "__main__":
    queue_main()