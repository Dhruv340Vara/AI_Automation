import time

from automation.worker.job import Job
from automation.worker.job_queue import JobQueue
from automation.worker.worker import Worker


def hello(name):

    print("Hello", name)


def run():

    queue = JobQueue()

    worker = Worker("QueueWorker")

    worker.start(queue)

    queue.put(Job(hello, "Dhruv"))

    queue.put(Job(hello, "AI"))

    time.sleep(1)

    worker.stop()

    worker.join()

    print(worker)


if __name__ == "__main__":
    run()
