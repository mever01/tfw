from contextlib import nullcontext
from typing import Any


class NullReporter:

    """
    Optional no-op Reporter implementation.

    Currently not used by the framework itself.
    Useful when consumer code expects a Reporter,
    but reporting should be disabled.
    """

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
