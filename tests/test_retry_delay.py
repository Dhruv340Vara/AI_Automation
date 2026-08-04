import time

from automation.worker.job import Job
from automation.worker.job_queue import JobQueue
from automation.worker.worker import Worker


counter = 0


def unstable():

    global counter

    counter += 1

    print(
        "Attempt",
        counter,
        round(time.time(), 1),
    )

    if counter < 3:
        raise RuntimeError()

    print("Success")


def run():

    queue = JobQueue()

    worker = Worker()

    worker.start(queue)

    queue.put(

        Job(

            unstable,

            max_retries=2,

            retry_delay=2,

        )

    )

    time.sleep(7)

    worker.stop()

    worker.join()


if __name__ == "__main__":
    run()
