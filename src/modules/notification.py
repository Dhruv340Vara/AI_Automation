import subprocess


def notify(title, content):

    try:

        subprocess.run(
            [
                "termux-notification",
                "--title", title,
                "--content", content
            ],
            capture_output=True,
            text=True
        )

        return {
            "status": "success",
            "title": title,
            "content": content
        }

    except Exception as e:

        return {
            "error": str(e)
        }
