import time

from automation.scheduler.timer import Timer


def run():

    print(Timer.now())

    print(type(Timer.timestamp()))

    start = Timer.timestamp()

    Timer.sleep(2)

    print(round(Timer.elapsed(start), 2))

    print(Timer.is_due(Timer.now()))

    print(Timer.format(Timer.now()))


if __name__ == "__main__":
    run()
