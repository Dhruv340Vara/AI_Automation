import time

from automation.scheduler.scheduler import Scheduler


def run():

    scheduler = Scheduler()

    scheduler.set_poll_interval(10)

    start = time.time()

    scheduler.start()

    time.sleep(1)

    scheduler.stop()

    elapsed = time.time() - start

    print(round(elapsed, 2))


if __name__ == "__main__":
    run()
