'''
This library provides a beautiful time estimator

Example Usage

import lemonbar
import time
n = 100
bar = lemonbar.Estimator(n, bar=True, permanent=True)
for i in range(n):
    bar.next()
    time.sleep(0.25)

>>> Complete: 99.0%  99 of 100. Estimated time remaining 0:00:00.249

'''

from datetime import datetime

class Lemonbar:
    # total number of things to count, starting count, show progress bar, \r or \n after printing bar
    def __init__(self, total, count=0, bar=False, permanent=False):
        self.total = total
        self.count = count
        self.start_time = datetime.now()
        self.permanent = permanent

    def show(self):
        terminator = '\r'
        if self.permanent:
            terminator = '\n'
        try:
            estimated_time_remaining = ((datetime.now() - self.start_time) / self.count) * (self.total - self.count)
        except ZeroDivisionError:
            # This happens if you call show() immediately after creating the Estimator
            estimated_time_remaining = None
        length_of_count = len(str(self.total))
        print(f'Complete: {str(self.count/self.total*100)[:6]}% {self.count:>{length_of_count}} of {self.total}. Estimated time remaining {str(estimated_time_remaining)[:(len(str(estimated_time_remaining))-3)]}', end=terminator)

    def next(self):
        self.count += 1
        self.show()
        if self.count == self.total:
            self.finish()

    def finish(self):
        runtime = datetime.now() - self.start_time
        print()
        print(f'Finished in {runtime}')

class StartEnd:
    def __init__(self, name='timer'):
        self.start_time = datetime.now()
        self.name = name
    def end(self):
        end_time = datetime.now()
        print(f' [{self.name}] took {end_time - self.start_time}')
