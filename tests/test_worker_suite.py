from tests.test_job_queue import run as job_queue_test
from tests.test_worker_queue import run as worker_queue_test
from tests.test_worker_retry import run as worker_retry_test
from tests.test_worker_fail import run as worker_fail_test


TESTS = [

    ("Job Queue", job_queue_test),

    ("Worker Queue", worker_queue_test),

    ("Worker Retry", worker_retry_test),

    ("Worker Fail", worker_fail_test),

]


def run():

    passed = 0

    failed = 0

    print("=" * 60)

    print("              Worker Test Suite")

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

        print("🎉 Worker System VERIFIED")

    print("=" * 60)


if __name__ == "__main__":

    run()
