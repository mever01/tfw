from typing import Generic

from tfw.assertions.base import BaseExpectation, T


class ValueExpectation(BaseExpectation[T], Generic[T]):

    def equal(self, expected: T):
        self._assert(
            self.actual == expected,
            expectation=f"to equal {expected!r}",
            negated_expectation=f"not to equal {expected!r}",
        )

    def is_none(self):
        self._assert(
            self.actual is None,
            expectation="to be None",
            negated_expectation="not to be None",
        )

    def is_instance_of(self, expected_type: type):
        self._assert(
            isinstance(self.actual, expected_type),
            expectation=f"to be instance of {expected_type.__name__}",
            negated_expectation=f"not to be instance of {expected_type.__name__}",
        )

    def is_same_as(self, expected: T):
        self._assert(
            self.actual is expected,
            expectation=f"to be the same object as {expected!r}",
            negated_expectation=f"not to be the same object as {expected!r}",
        )
