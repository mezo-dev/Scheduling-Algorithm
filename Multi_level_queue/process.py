from states import State


class Process:
    _next_id = 1

    def __init__(self, name: str, arrival_time: int, burst_time: int) -> None:
        self.id = Process._next_id
        Process._next_id += 1
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
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


def run_process(process: Process, quantum: int) -> bool:
    cpu_time = min(process.remaining_time, quantum)

    print(
        f"Running {process.name} "
        f"for {cpu_time} units "
        f"(remaining before={process.remaining_time})"
    )

    process.remaining_time -= cpu_time
    process.mark_as_running()

    if process.remaining_time == 0:
        process.mark_as_terminated()
        print(f"{process.name} Finished.\n")
        return True
    else:
        print(
            f"Running {process.name} "
            f"for {cpu_time} units "
            f"(remaining before={process.remaining_time})"
        )
        return False
