import threading

class SquaredSumWorker(threading.Thread):
    def __init__(self, n, **kwargs):
        self._n = n
        super(SquaredSumWorker, self).__init__(**kwargs)  # can be used for passing params to thread class
        self.start()

    def _calculate_sum_of_squares(self):
        s = 0
        for i in range(self._n):
            s += i ** 2
        print(s)

    def run(self):
        self._calculate_sum_of_squares()
