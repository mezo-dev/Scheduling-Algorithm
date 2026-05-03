from .process import Process


class Queue:
    def __init__(self, process: Process, quantum: int = 8): ...
