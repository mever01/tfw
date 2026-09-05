import re

from src.assertions.value import ValueExpectation


class StringExpectation(ValueExpectation[str]):

    def contains(self, expected: str):
        self._assert(
            expected in self.actual,
            expectation=f"to contain {expected!r}",
            negated_expectation=f"not to contain {expected!r}",
        )

    def starts_with(self, expected: str):
        self._assert(
            self.actual.startswith(expected),
            expectation=f"to start with {expected!r}",
            negated_expectation=f"not to start with {expected!r}",
        )

    def ends_with(self, expected: str):
        self._assert(
            self.actual.endswith(expected),
            expectation=f"to end with {expected!r}",
            negated_expectation=f"not to end with {expected!r}",
        )

    def is_empty(self):
        self._assert(
            self.actual == "",
            expectation="to be empty",
            negated_expectation="not to be empty",
        )

    def has_length(self, expected: int):
        self._assert(
            len(self.actual) == expected,
            expectation=f"to have length {expected}",
            negated_expectation=f"not to have length {expected}",
        )

    def matches(self, pattern: str):
        self._assert(
            re.search(pattern, self.actual) is not None,
            expectation=f"to match pattern {pattern!r}",
            negated_expectation=f"not to match pattern {pattern!r}",
        )
