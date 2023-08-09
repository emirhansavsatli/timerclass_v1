import threading
import time

class Timer:
    def __init__(self,seconds):
        self.seconds = seconds
        self.timeout = False
        self.thread = None


    def stop(self):
        self.timeout = True

    def timer_thread(self):
        star_time = time.time()
        while not self.timeout:
            elapsed = time.time()-star_time
            if elapsed >= self.seconds:
                self.timeout = True
                break

    def start(self):
        if self.thread is None:
            self.timeout = False
            self.thread = threading.Thread(target=self.timer_thread)
            self.thread.start()





