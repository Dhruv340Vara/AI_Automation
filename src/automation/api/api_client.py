from __future__ import annotations

import requests


class APIClient:
    """
    Simple REST API client.
    """

    def request(
        self,
        trigger,
    ):

        response = requests.request(

            method=trigger.method,

            url=trigger.url,

            headers=trigger.headers,

            params=trigger.params,

            json=trigger.body,

            timeout=trigger.timeout,

        )

        return response
