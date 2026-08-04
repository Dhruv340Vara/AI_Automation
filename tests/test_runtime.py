from automation.runtime.automation_runtime import (
    AutomationRuntime,
)


def run():

    runtime = AutomationRuntime()

    print(runtime)

    print(runtime.start())

    print(runtime.is_running)

    print(runtime.stop())

    print(runtime.is_running)

    print(runtime)


if __name__ == "__main__":

    run()
