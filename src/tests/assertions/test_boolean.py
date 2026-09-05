import unittest

from src.assertions.boolean import BooleanExpectation


class BooleanExpectationTests(unittest.TestCase):

    @staticmethod
    def test_is_true():
        expectation = BooleanExpectation(True)

        expectation.is_true()

    @staticmethod
    def test_is_false():
        expectation = BooleanExpectation(False)

        expectation.is_false()

    def test_is_true_raises_assertion_error(self):
        expectation = BooleanExpectation(False)

        with self.assertRaises(AssertionError):
            expectation.is_true()

    def test_is_false_raises_assertion_error(self):
        expectation = BooleanExpectation(True)

        with self.assertRaises(AssertionError):
            expectation.is_false()
