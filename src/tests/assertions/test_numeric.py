import unittest
from decimal import Decimal

from src.assertions.numeric import NumericExpectation


class NumericExpectationTests(unittest.TestCase):

    @staticmethod
    def test_greater_than():
        """Checks that the actual value is greater than the expected value."""
        expectation = NumericExpectation(10)

        expectation.greater_than(5)

    @staticmethod
    def test_greater_than_or_equal():
        """Checks that the actual value is greater than or equal to the expected value."""
        expectation = NumericExpectation(10)

        expectation.greater_than_or_equal(10)

    @staticmethod
    def test_less_than():
        """Checks that the actual value is less than the expected value."""
        expectation = NumericExpectation(5)

        expectation.less_than(10)

    @staticmethod
    def test_less_than_or_equal():
        """Checks that the actual value is less than or equal to the expected value."""
        expectation = NumericExpectation(10)

        expectation.less_than_or_equal(10)

    @staticmethod
    def test_between_inclusive():
        """Checks that the actual value is within the inclusive range."""
        expectation = NumericExpectation(10)

        expectation.between(5, 10)

    def test_between_exclusive(self):
        """Checks that the exclusive range assertion fails on the boundary value."""
        expectation = NumericExpectation(10)

        with self.assertRaises(AssertionError):
            expectation.between(5, 10, inclusive=False)

    @staticmethod
    def test_positive():
        """Checks that the actual value is positive."""
        expectation = NumericExpectation(10)

        expectation.positive()

    @staticmethod
    def test_negative():
        """Checks that the actual value is negative."""
        expectation = NumericExpectation(-10)

        expectation.negative()

    @staticmethod
    def test_zero():
        """Checks that the actual value is zero."""
        expectation = NumericExpectation(0)

        expectation.zero()

    @staticmethod
    def test_decimal():
        """Checks numeric assertions with Decimal values."""
        expectation = NumericExpectation(
            Decimal("10.5")
        )

        expectation.greater_than(
            Decimal("10.0")
        )

    def test_greater_than_raises_for_equal_values(self):
        """Checks that greater_than() rejects an equal value."""
        expectation = NumericExpectation(10)

        with self.assertRaises(AssertionError):
            expectation.greater_than(10)

    def test_less_than_raises_for_equal_values(self):
        """Checks that less_than() rejects an equal value."""
        expectation = NumericExpectation(10)

        with self.assertRaises(AssertionError):
            expectation.less_than(10)
