import subprocess

def torch_on():
    try:
        result = subprocess.run(
            ["termux-torch", "on"],
            capture_output=True,
            text=True
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {
            "error": str(e)
        }


def torch_off():
    try:
        subprocess.run(
            ["termux-torch", "off"],
            capture_output=True,
            text=True
        )

        return {
            "status": "success",
            "torch": "off"
        }

    except Exception as e:
        return {
            "error": str(e)
        }
