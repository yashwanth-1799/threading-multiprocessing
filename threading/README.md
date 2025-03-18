
### Sync Code Output
```
1000000000000000000
8000000000000000000
27000000000000000000
64000000000000000000
125000000000000000000
Time taken for sum of squares 8.6
Time taken for sleep 15.0
```

### Threading Approach Output
```
1000000000000000000
8000000000000000000
27000000000000000000
64000000000000000000
125000000000000000000
Time taken for sum of squares 4.7
Time taken for sleep 5.0
```

###### When we set daemon to True the thread stops executing when the main thread has completed execution
```
t=threading.Thread(target=calculate_sum_of_squares, args=(val,) daemon=True)
```

###### Join waits for the thread to complete before proceeding further
```
t=threading.Thread(target=calculate_sum_of_squares, args=(val,))
t.start()
t.join()
```