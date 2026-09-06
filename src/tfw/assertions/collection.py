from collections.abc import Collection
from typing import Generic, TypeVar

from tfw.assertions.value import ValueExpectation


ItemT = TypeVar("ItemT")


class CollectionExpectation(
    ValueExpectation[Collection[ItemT]],
    Generic[ItemT],
):

    def __init__(self, actual: Collection[ItemT]):
        super().__init__(actual)

    def contains(self, expected: ItemT):
        self._assert(
            expected in self.actual,
            expectation=f"to contain {expected!r}",
            negated_expectation=f"not to contain {expected!r}",
        )

    def contains_all(self, expected: Collection[ItemT]):
        missing = [
            item
            for item in expected
            if item not in self.actual
        ]

        self._assert(
            not missing,
            expectation=f"to contain all items {expected!r}",
            negated_expectation=f"not to contain all items {expected!r}",
        )

    def has_length(self, expected: int):
        self._assert(
            len(self.actual) == expected,
            expectation=f"to have length {expected}",
            negated_expectation=f"not to have length {expected}",
        )

    def is_empty(self):
        self._assert(
            len(self.actual) == 0,
            expectation="to be empty",
            negated_expectation="not to be empty",
        )
