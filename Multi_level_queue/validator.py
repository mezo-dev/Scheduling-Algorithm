from .process import Process
import time


class QueueValidator:
    queue_quantium_8 = 8
    queue_quantium_16 = 16

    @staticmethod
    def validate_burst_time_quantium(process: Process):
        if process.burst_time <= QueueValidator.queue_quantium_8:
            print("Process is Running...")
            process.mark_as_running()
            time.sleep(3)
            print("Process is Terminated...")
            process.mark_as_terminated()
