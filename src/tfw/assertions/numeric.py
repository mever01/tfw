from decimal import Decimal
from typing import TypeVar

from tfw.assertions.value import ValueExpectation


NumericT = TypeVar(
    "NumericT",
    int,
    float,
    Decimal,
)


class NumericExpectation(ValueExpectation[NumericT]):

    def greater_than(self, expected: NumericT):
        self._assert(
            self.actual > expected,
            expectation=f"to be greater than {expected!r}",
            negated_expectation=f"to be less than or equal to {expected!r}",
        )

    def greater_than_or_equal(self, expected: NumericT):
        self._assert(
            self.actual >= expected,
            expectation=f"to be greater than or equal to {expected!r}",
            negated_expectation=f"to be less than {expected!r}",
        )

    def less_than(self, expected: NumericT):
        self._assert(
            self.actual < expected,
            expectation=f"to be less than {expected!r}",
            negated_expectation=f"to be greater than or equal to {expected!r}",
        )

    def less_than_or_equal(self, expected: NumericT):
        self._assert(
            self.actual <= expected,
            expectation=f"to be less than or equal to {expected!r}",
            negated_expectation=f"to be greater than {expected!r}",
        )

    def between(
        self,
        minimum: NumericT,
        maximum: NumericT,
        *,
        inclusive: bool = True,
    ):
        if inclusive:
            condition = minimum <= self.actual <= maximum
            expectation = (
                f"to be between {minimum!r} and {maximum!r} inclusively"
            )
            negated_expectation = (
                f"not to be between {minimum!r} and {maximum!r} inclusively"
            )
        else:
            condition = minimum < self.actual < maximum
            expectation = (
                f"to be between {minimum!r} and {maximum!r} exclusively"
            )
            negated_expectation = (
                f"not to be between {minimum!r} and {maximum!r} exclusively"
            )

        self._assert(
            condition,
            expectation=expectation,
            negated_expectation=negated_expectation,
        )

    def positive(self):
        self._assert(
            self.actual > 0,
            expectation="to be positive",
            negated_expectation="not to be positive",
        )

    def negative(self):
        self._assert(
            self.actual < 0,
            expectation="to be negative",
            negated_expectation="not to be negative",
        )

    def zero(self):
        self._assert(
            self.actual == 0,
            expectation="to be zero",
            negated_expectation="not to be zero",
        )
