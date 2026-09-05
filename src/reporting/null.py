from contextlib import nullcontext
from typing import Any


class NullReporter:

    # Instance method intentionally kept to satisfy the Reporter contract.
    # noinspection PyMethodMayBeStatic
    def step(self, name: str):
        return nullcontext()

    def attach_text(
        self,
        name: str,
        content: str,
    ):
        pass

    def attach_json(
        self,
        name: str,
        content: Any,
    ):
        pass
