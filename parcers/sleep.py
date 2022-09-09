from time import sleep, time

class Sleeper:
    iteration_time = 0
    prev_time = 0
    TIME_BETWEEN_ITERATIONS = 0

    def __init__(self, time_to_sleep):
        self.TIME_BETWEEN_ITERATIONS = time_to_sleep
        self.prev_time = time()

    def sleep_for_time(self):
        self.iteration_time = time() - self.prev_time
        self.time_to_sleep = self.TIME_BETWEEN_ITERATIONS - self.iteration_time

        if self.time_to_sleep < 0:
            self.time_to_sleep = 0
        
        sleep(self.time_to_sleep)
        # print(f'i just slept for {self.time_to_sleep} + {self.iteration_time}')
        self.prev_time = time()
        return self.time_to_sleep

