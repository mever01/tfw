from contextlib import AbstractContextManager
from typing import Any, Protocol


class Reporter(Protocol):

    def step(
        self,
        name: str,
    ) -> AbstractContextManager:
        ...

    def attach_text(
        self,
        name: str,
        content: str,
    ):
        ...

    def attach_json(
        self,
        name: str,
        content: Any,
    ):
        ...
