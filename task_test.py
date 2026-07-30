from automation.tasks.base_task import BaseTask
from automation.tasks.task_result import TaskResult


class HelloTask(BaseTask):

    def run(self):

        print("Hello Automation")

        return TaskResult(
            success=True,
            message="Task completed successfully."
        )


task = HelloTask("Demo Task")

result = task.execute()

print(task.to_dict())
print(result.to_dict())
print(task.execution_time())
