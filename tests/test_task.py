from automation.tasks.base_task import BaseTask
from automation.tasks.task_result import TaskResult


class DemoTask(BaseTask):

    def run(self):

        return TaskResult(
            success=True,
            message="Task OK"
        )


def run():

    task = DemoTask("Demo")

    result = task.execute()

    assert result.success

    assert task.status.value == "success"

    return True
