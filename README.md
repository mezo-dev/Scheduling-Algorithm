# Multilevel Queue Scheduler

A small simulation of a Multilevel Feedback Queue (MLFQ) CPU scheduler in Python.

## How it works

There are three queues, each with its own time slice (quantum):

| Queue | Quantum |
|-------|---------|
| Q0    | 8       |
| Q1    | 12      |
| Q2    | 16      |

Every process starts in Q0. It runs for one quantum:

- If it finishes, it's done.
- If it doesn't finish, it drops down to the next queue (Q0 → Q1 → Q2).

Q0 always runs first. A queue only gets the CPU when the queues above it are empty. Processes that reach Q2 keep cycling there until they finish.

## Requirements

Python 3.

## Running it

With [just](https://github.com/casey/just):

```
just run
```

Or directly:

```
python3 scheduler.py
```

The processes are defined at the bottom of `scheduler.py`:

```python
q0.append(Process("Process 1", 2, 7))    # name, arrival time, burst time
q0.append(Process("Process 2", 5, 14))
q0.append(Process("Process 3", 8, 23))
```

Change the burst times (the third number) to try different runs.

## Example output

```
python3 scheduler.py
Running Process 1 for 7 units (remaining before=7)
Process 1 Finished.

Running Process 2 for 8 units (remaining before=14)
Running Process 2 for 8 units (remaining before=6)
Moved Process 2 to Q1

Running Process 3 for 8 units (remaining before=23)
Running Process 3 for 8 units (remaining before=15)
Moved Process 3 to Q1

Running Process 2 for 6 units (remaining before=6)
Process 2 Finished.

Running Process 3 for 12 units (remaining before=15)
Running Process 3 for 12 units (remaining before=3)
Moved Process 3 to Q2

Running Process 3 for 3 units (remaining before=3)
Process 3 Finished.
```

Process 1 finishes in Q0. Process 2 and 3 are too long, so they drop down a queue each round until they're done.
