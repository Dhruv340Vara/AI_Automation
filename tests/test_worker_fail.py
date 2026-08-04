import time

from automation.worker.job import Job
from automation.worker.worker import Worker
from automation.worker.job_queue import JobQueue


def always_fail():

    print("Fail")

    raise RuntimeError()


def run():

    queue = JobQueue()

    worker = Worker()

    worker.start(queue)

    job = Job(
        always_fail,
        max_retries=1,
    )

    queue.put(job)

    time.sleep(2)

    worker.stop()

    worker.join()

    print(job.attempts)

    print(job.error is not None)


if __name__ == "__main__":
    run()
