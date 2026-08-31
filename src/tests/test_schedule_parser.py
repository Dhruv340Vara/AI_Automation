from automation.scheduler.schedule_parser import ScheduleParser

print(ScheduleParser.after_seconds(30))
print()

print(ScheduleParser.after_minutes(5))
print()

print(ScheduleParser.after_hours(2))
print()

print(ScheduleParser.interval(60))
print()

print(ScheduleParser.daily(9, 0))
print()

print(ScheduleParser.weekly(0, 10, 30))
print()

print(ScheduleParser.monthly(15, 14, 0))
