from tests.test_timer import run as timer_test
from tests.test_timer_scheduler import run as scheduler_timer_test
from tests.test_interruptible_timer import run as interruptible_timer_test


TESTS = [
    ("Timer", timer_test),
    ("Scheduler Timer", scheduler_timer_test),
    ("Interruptible Timer", interruptible_timer_test),
]


def run():

    passed = 0
    failed = 0

    print("=" * 60)
    print("               Timer Test Suite")
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
        print("🎉 Timer System VERIFIED")

    print("=" * 60)


if __name__ == "__main__":
    run()
