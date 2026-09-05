import unittest

from src.assertions.value import ValueExpectation


class ValueExpectationTests(unittest.TestCase):

    @staticmethod
    def test_equal():
        """Checks successful comparison of equal values."""
        expectation = ValueExpectation(10)

        expectation.equal(10)

    def test_equal_raises_assertion_error(self):
        """Checks that equal() raises for different values."""
        expectation = ValueExpectation(10)

        with self.assertRaises(AssertionError):
            expectation.equal(20)

    @staticmethod
    def test_not_equal():
        """Checks successful negated comparison of different values."""
        expectation = ValueExpectation(10)

        expectation.not_.equal(20)

    def test_not_equal_raises_assertion_error(self):
        """Checks that not_.equal() raises for equal values."""
        expectation = ValueExpectation(10)

        with self.assertRaises(AssertionError):
            expectation.not_.equal(10)

    @staticmethod
    def test_negation_resets_after_successful_assertion():
        """Checks that negation resets after a successful assertion."""
        expectation = ValueExpectation(10)

        expectation.not_.equal(20)
        expectation.equal(10)

    def test_negation_resets_after_failed_assertion(self):
        """Checks that negation resets even after an AssertionError."""
        expectation = ValueExpectation(10)

        with self.assertRaises(AssertionError):
            expectation.not_.equal(10)

        expectation.equal(10)