from process import Process
from collections import deque

q0 = deque()
q1 = deque()
q2 = deque()

QUANTUMS = [8, 12, 16]

q0.append(Process("Process 1", 2, 7))
q0.append(Process("Process 2", 5, 14))
q0.append(Process("Process 3", 8, 23))
