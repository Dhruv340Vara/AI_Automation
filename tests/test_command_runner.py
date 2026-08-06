from automation.devices import (
    CommandRunner,
)

runner = CommandRunner()

print(runner)

print()

print("PWD")

result = runner.run(
    ["pwd"]
)

print(result.stdout.strip())

print()

print("Python Exists")

print(

    runner.exists(

        "python3"

    )

)

print()

print("Python Path")

print(

    runner.which(

        "python3"

    )

)

print()

print("Start Firefox")

if runner.exists("firefox"):

    runner.start(
        ["firefox"]
    )

    print("Started")

else:

    print("Firefox not installed")

print()

print("Shell Command")

result = runner.shell(
    "echo Hello Assistant"
)

print(
    result.stdout.strip()
)
