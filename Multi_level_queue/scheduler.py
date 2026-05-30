from queue import q0, q1, q2, QUANTUMS
from process import run_process
from process import Process


def scheduler():
    while q0 or q1 or q2:
        if q0:
            process = q0.popleft()
            finished = run_process(process, QUANTUMS[0])

            if not finished:
                process.mark_as_waiting()
                q1.append(process)
                print(f"Moved {process.name} to Q1\n")

        elif q1:
            process = q1.popleft()

            finished = run_process(process, QUANTUMS[1])

            if not finished:
                process.mark_as_waiting()
                q2.append(process)
                print(f"Moved {process.name} to Q2\n")

        elif q2:
            process = q2.popleft()

            finished = run_process(process, QUANTUMS[2])

            if not finished:
                process.mark_as_waiting()
                q2.append(process)
                print(f"Returned {process.name} to Q2\n")


q0.append(Process("Process 1", 2, 7))
q0.append(Process("Process 2", 5, 14))
q0.append(Process("Process 3", 8, 23))

scheduler()
