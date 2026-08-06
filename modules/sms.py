import subprocess


def send_sms(number, message):

    try:

        result = subprocess.run(
            [
                "termux-sms-send",
                "-n",
                number,
                message
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            return {
                "status": "success",
                "number": number,
                "message": message
            }

        return {
            "status": "failed",
            "error": result.stderr.strip()
        }

    except Exception as e:

        return {
            "error": str(e)
        }
