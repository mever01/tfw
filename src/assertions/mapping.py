from collections.abc import Mapping
from typing import Generic, TypeVar

from src.assertions.value import ValueExpectation


KeyT = TypeVar("KeyT")
ValueT = TypeVar("ValueT")


class MappingExpectation(
    ValueExpectation[Mapping[KeyT, ValueT]],
    Generic[KeyT, ValueT],
):

    def has_key(self, expected: KeyT):
        self._assert(
            expected in self.actual,
            expectation=f"to have key {expected!r}",
            negated_expectation=f"not to have key {expected!r}",
        )

    def has_keys(self, expected: set[KeyT]):
        self._assert(
            expected.issubset(self.actual.keys()),
            expectation=f"to have keys {expected!r}",
            negated_expectation=f"not to have all keys {expected!r}",
        )

    def has_value(self, expected: ValueT):
        self._assert(
            expected in self.actual.values(),
            expectation=f"to have value {expected!r}",
            negated_expectation=f"not to have value {expected!r}",
        )

    def contains_item(
        self,
        key: KeyT,
        value: ValueT,
    ):
        condition = (
            key in self.actual
            and self.actual[key] == value
        )

        self._assert(
            condition,
            expectation=f"to contain item {key!r}: {value!r}",
            negated_expectation=f"not to contain item {key!r}: {value!r}",
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
