import subprocess


def run_termux(command):
    """Run a Termux command and return output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()

        return result.stderr.strip()

    except Exception as e:
        return str(e)


def get_device_info():
    return {
        "manufacturer": run_termux("getprop ro.product.manufacturer"),
        "model": run_termux("getprop ro.product.model"),
        "android_version": run_termux("getprop ro.build.version.release"),
        "sdk": run_termux("getprop ro.build.version.sdk"),
        "device": run_termux("getprop ro.product.device"),
        "board": run_termux("getprop ro.product.board"),
        "cpu": run_termux("getprop ro.hardware"),
        "kernel": run_termux("uname -r")
    }
