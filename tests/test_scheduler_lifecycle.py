import time

from automation.scheduler.scheduler import Scheduler

scheduler = Scheduler()

print(scheduler.is_running)

print(scheduler.start())

print(scheduler.is_running)

time.sleep(3)

print(scheduler.stop())

print(scheduler.is_running)
