import time

from automation.worker.job import Job
from automation.worker.worker_pool import WorkerPool


def hello(name):

    print("Hello", name)

    time.sleep(1)


def run():

    pool = WorkerPool(size=2)

    print(pool)

    pool.start()

    pool.submit(Job(hello, "Dhruv"))

    pool.submit(Job(hello, "AI"))

    pool.submit(Job(hello, "Automation"))

    time.sleep(3)

    pool.stop()

    print(pool)


if __name__ == "__main__":
    run()
