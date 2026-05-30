from .states import State


class Process:
    _next_id = 1

    def __init__(self, arrival_time: int, burst_time: int) -> None:
        self.id = Process._next_id
        Process._next_id += 1
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.state = State.READY

    @classmethod
    def reset_ids(cls) -> None:
        cls._next_id = 1

    def mark_as_running(self):
        self.state = State.RUNNING

    def mark_as_waiting(self):
        self.state = State.WAITING

    def mark_as_terminated(self):
        self.state = State.TERMINATED

    def execute(self):
        print(f"Executing Process {self.id}...")
