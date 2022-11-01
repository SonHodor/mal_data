from time import sleep, time

class Sleeper:
    iteration_time = 0
    prev_time = 0
    TIME_BETWEEN_ITERATIONS = 0

    last_time = 0


    def __init__(self, time_to_sleep):
        self.TIME_BETWEEN_ITERATIONS = time_to_sleep
        self.prev_time = time()
        self.last_time = self.prev_time


    def sleep_for_time(self):
        self.iteration_time = time() - self.prev_time
        self.time_to_sleep = self.TIME_BETWEEN_ITERATIONS - self.iteration_time

        if self.time_to_sleep < 0:
            self.time_to_sleep = 0
        
        sleep(self.time_to_sleep)
        
        self.prev_time = time()
        return self.time_to_sleep
    
    
    def time_since_last_time(self, to_ping=False):
        now = time()
        time_passed = now - self.last_time
        self.last_time = now
        if to_ping:
            return int(time_passed * 1000)
        else:
            time_passed
