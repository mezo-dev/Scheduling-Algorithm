class Process:
    _next_id = 1

    def __init__(self, arrival_time: int, burst_time: int) -> None:
        self.id = Process._next_id
        Process._next_id += 1
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    @classmethod
    def reset_ids(cls) -> None:
        cls._next_id = 1
