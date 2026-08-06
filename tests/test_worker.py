import time

from automation.worker.worker import Worker


def job():

    print("Job Started")

    time.sleep(2)

    print("Job Finished")


def run():

    worker = Worker("DemoWorker")

    print(worker)

    worker.start(job)

    print(worker.is_running)

    worker.join()

    print(worker.is_running)

    print(worker)


if __name__ == "__main__":
    run()
