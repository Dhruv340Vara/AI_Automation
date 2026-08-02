from automation.worker.job import Job
from automation.worker.job_queue import JobQueue


def hello(name):

    print("Hello", name)


def run():

    queue = JobQueue()

    job1 = Job(
        hello,
        "Dhruv"
    )

    job2 = Job(
        hello,
        "AI"
    )

    queue.put(job1)

    queue.put(job2)

    print(queue)

    while not queue.empty():

        job = queue.get()

        job.execute()

        queue.task_done()

    print(queue)


if __name__ == "__main__":
    run()
