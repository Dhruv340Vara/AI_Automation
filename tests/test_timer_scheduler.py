import time

from automation.scheduler.scheduler import Scheduler


def run():

    scheduler = Scheduler()

    scheduler.set_poll_interval(0.5)

    print("Starting...")

    scheduler.start()

    time.sleep(2)

    print("Running:", scheduler.is_running)

    scheduler.stop()

    print("Stopped:", scheduler.is_running)


if __name__ == "__main__":
    run()
