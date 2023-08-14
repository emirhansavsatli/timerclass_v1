import threading
import time

class Timer:
    def __init__(self,seconds):
        self.seconds = seconds
        self.timeout = False
        self.thread = None

    def reset(self):
        self.timeout = False
        self.timeout = False
        self.thread = None
        self.start()

    def force_stop(self):
        self.timeout = True
        if self.thread and self.thread.is_alive():
            self.thread.join()

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
        if self.thread is None or not self.thread.is_alive():
            self.timeout = False
            self.thread = threading.Thread(target=self.timer_thread)
            self.thread.start()





