from tests.test_task import run as task_test
from tests.test_automation_model import run as model_test
from tests.test_manager import run as manager_test
from tests.test_storage import run as storage_test
from tests.test_core import run as core_test


tests = [
    ("Task", task_test),
    ("Automation Model", model_test),
    ("Manager", manager_test),
    ("Storage", storage_test),
    ("Core API", core_test),
]

passed = 0
failed = 0

print("=" * 60)
print("Automation Test Suite")
print("=" * 60)

for name, test in tests:

    try:

        test()

        print(f"✅ {name}")

        passed += 1

    except Exception as exc:

        print(f"❌ {name}")

        print(exc)

        failed += 1

print("=" * 60)

print("Passed :", passed)

print("Failed :", failed)

print("Total  :", len(tests))

if failed == 0:

    print("\n🎉 Automation Core VERIFIED")

else:

    print("\n⚠ Some tests failed.")

print("=" * 60)
