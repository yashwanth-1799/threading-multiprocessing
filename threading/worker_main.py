import time

from workers.sleep_workers import SleepWorker
from workers.squared_sum_workers import SquaredSumWorker

def threading_main():
    calc_start_time = time.time()

    current_threads = []
    for i in range(5):
        val = (i+1)*1000000
        square_sum_worker = SquaredSumWorker(val)
        current_threads.append(square_sum_worker)

    for t in current_threads:
        t.join()

    print(f"Time taken for sum of squares {round(time.time()-calc_start_time, 1)}")

    current_threads = []
    sleep_start_time = time.time()
    for i in range(1, 6):
        sleep_worker = SleepWorker(i)
        current_threads.append(sleep_worker)

    for t in current_threads:
        t.join()

    print(f"Time taken for sleep {round(time.time()-sleep_start_time, 1)}")

if __name__ =="__main__":
    threading_main()