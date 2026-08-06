import subprocess


def run(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

    except Exception as e:
        return str(e)


def get_storage_info():

    output = run("df -h /storage/emulated/0")

    if not output:
        return {"error": "Unable to read storage"}

    lines = output.splitlines()

    if len(lines) < 2:
        return {"error": "Invalid storage data"}

    parts = lines[1].split()

    return {
        "filesystem": parts[0],
        "total": parts[1],
        "used": parts[2],
        "available": parts[3],
        "usage_percent": parts[4],
        "mount": parts[5]
    }
