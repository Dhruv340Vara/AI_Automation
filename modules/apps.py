import subprocess

class AppManager:

    def open_app(self, app_name):
        result = subprocess.run(
            [
                "termux-open-app",
                app_name
            ],
            capture_output=True,
            text=True
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
