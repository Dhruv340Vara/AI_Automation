import time

from automation.worker.job import Job
from automation.worker.worker import Worker
from automation.worker.job_queue import JobQueue


counter = 0


def unstable():

    global counter

    counter += 1

    print("Attempt", counter)

    if counter < 3:

        raise RuntimeError("Failed")

    print("Success")


def run():

    queue = JobQueue()

    worker = Worker()

    worker.start(queue)

    queue.put(
        Job(
            unstable,
            max_retries=2,
        )
    )

    time.sleep(3)

    worker.stop()

    worker.join()


if __name__ == "__main__":
    run()
