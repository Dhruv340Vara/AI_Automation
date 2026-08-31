from __future__ import annotations

import threading
import time

import requests

from automation.events.api_event import (
    APIEventFactory,
)

from automation.api.api_client import (
    APIClient,
)


class APIPoller:

    """
    Periodically polls an API.

    Emits API events into runtime.
    """

    def __init__(
        self,
        trigger,
        runtime,
    ):

        self.trigger = trigger

        self.runtime = runtime

        self.client = APIClient()

        self._running = False

        self._thread = None

    # ---------------------------- #

    @property
    def is_running(self):

        return self._running

    # ---------------------------- #

    def start(self):

        if self._running:
            return False

        self._running = True

        self._thread = threading.Thread(

            target=self._run,

            daemon=True,

            name=f"APIPoller:{self.trigger.name}",

        )

        self._thread.start()

        return True

    # ---------------------------- #

    def stop(self):

        if not self._running:
            return False

        self._running = False

        self._thread.join()

        return True

    # ---------------------------- #

    def _run(self):

        while self._running:

            try:

                response = self.client.request(
                    self.trigger
                )

                try:

                    data = response.json()

                except Exception:

                    data = {
                        "text": response.text,
                    }

                event = APIEventFactory.response(

                    url=self.trigger.url,

                    method=self.trigger.method,

                    status_code=response.status_code,

                    response=data,

                    headers=dict(response.headers),

                    elapsed=(
                        response.elapsed.total_seconds()
                    ),

                )

            except requests.Timeout:

                event = APIEventFactory.timeout(

                    self.trigger.url,

                    self.trigger.timeout,

                )

            except Exception as exc:

                event = APIEventFactory.error(

                    self.trigger.url,

                    self.trigger.method,

                    str(exc),

                )

            self.runtime.emit_event(
                event
            )

            time.sleep(
                self.trigger.interval
            )

    # ---------------------------- #

    def __repr__(self):

        state = (
            "running"
            if self._running
            else "stopped"
        )

        return (
            f"<APIPoller {state}>"
        )
