from tests.test_scheduler import run as scheduler_core
from tests.test_scheduler_lifecycle import run as lifecycle
from tests.test_schedule_parser import run as parser
from tests.test_due_tasks import run as due_tasks
from tests.test_dispatch import run as dispatch
from tests.test_dispatch_error import run as dispatch_error
from tests.test_execution_result import run as execution_result
from tests.test_execution_failed import run as execution_failed
from tests.test_execution_retry import run as execution_retry
from tests.test_reschedule import run as reschedule
from tests.test_monthly_schedule import run as monthly
from tests.test_monthly_leap import run as leap
from tests.test_cleanup import run as cleanup
from tests.test_cleanup_recurring import run as cleanup_recurring


TESTS = [

    ("Scheduler Core", scheduler_core),

    ("Lifecycle", lifecycle),

    ("Schedule Parser", parser),

    ("Due Tasks", due_tasks),

    ("Dispatch", dispatch),

    ("Dispatch Error", dispatch_error),

    ("Execution Result", execution_result),

    ("Execution Failed", execution_failed),

    ("Execution Retry", execution_retry),

    ("Recurring", reschedule),

    ("Monthly", monthly),

    ("Leap Year", leap),

    ("Cleanup", cleanup),

    ("Cleanup Recurring", cleanup_recurring),
]


def run():

    passed = 0

    failed = 0

    print("=" * 60)

    print("            Scheduler Test Suite")

    print("=" * 60)

    for name, test in TESTS:

        try:

            test()

            print(f"✅ {name}")

            passed += 1

        except Exception as e:

            print(f"❌ {name}")

            print(e)

            failed += 1

    print("=" * 60)

    print("Passed :", passed)

    print("Failed :", failed)

    print("Total  :", len(TESTS))

    if failed == 0:

        print()

        print("🎉 Scheduler VERIFIED")

    print("=" * 60)


if __name__ == "__main__":

    run()
