import time
import threading

def calculate_sum_of_squares(n):
    s=0
    for i in range(n):
        s+=i**2
    print(s)

def sleep_for(s):
    time.sleep(s)

def main():
    calc_start_time = time.time()
    for i in range(5):
        calculate_sum_of_squares((i+1)*1000000)

    print(f"Time taken for sum of squares {round(time.time()-calc_start_time, 1)}")

    sleep_start_time = time.time()
    for i in range(1, 6):
        sleep_for(i)
    print(f"Time taken for sleep {round(time.time()-sleep_start_time, 1)}")

def threading_main():
    calc_start_time = time.time()

    current_threads = []
    for i in range(5):
        val = (i+1)*1000000
        t=threading.Thread(target=calculate_sum_of_squares, args=(val,))
        t.start()
        current_threads.append(t)

    for t in current_threads:
        t.join()

    print(f"Time taken for sum of squares {round(time.time()-calc_start_time, 1)}")

    current_threads = []
    sleep_start_time = time.time()
    for i in range(1, 6):
        t=threading.Thread(target=sleep_for, args=(i,))
        t.start()
        current_threads.append(t)

    for t in current_threads:
        t.join()

    print(f"Time taken for sleep {round(time.time()-sleep_start_time, 1)}")

if __name__ =="__main__":
    threading_main()