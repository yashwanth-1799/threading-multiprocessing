import threading
import time

class SleepWorker(threading.Thread):
    def __init__(self, seconds, **kwargs):
        self._seconds = seconds
        super(SleepWorker, self).__init__(**kwargs)  # can be used for passing params to thread class
        self.start()

    def _sleep_for(self):
        time.sleep(self._seconds)

    def run(self):
        self._sleep_for()
