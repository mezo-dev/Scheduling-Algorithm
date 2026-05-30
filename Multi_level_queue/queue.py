from .process import Process


class Queue:
    def __init__(self):
        self.queue = []
        self.quantum = 8

    def add_process(self, process: Process):
        self.queue.append(process)
        process_time = process.burst_time - self.quantum
        if process_time == 0:
            process.execute()
        elif process_time < 0:
            ...
