import time

class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._end_time = None

    def start(self):
        self._start_time = time.time()
    
    def stop(self):
        self._end_time = time.time()

    @property
    def total_time(self):
        return self._end_time - self._start_time