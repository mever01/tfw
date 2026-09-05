import unittest

from src.assertions.string import StringExpectation


class StringExpectationTests(unittest.TestCase):

    @staticmethod
    def test_contains():
        """Checks that the string contains the expected substring."""
        expectation = StringExpectation("hello world")

        expectation.contains("world")

    def test_contains_raises_assertion_error(self):
        """Checks that contains() raises when the substring is missing."""
        expectation = StringExpectation("hello world")

        with self.assertRaises(AssertionError):
            expectation.contains("python")

    @staticmethod
    def test_not_contains():
        """Checks successful negated substring assertion."""
        expectation = StringExpectation("hello world")

        expectation.not_.contains("python")

    @staticmethod
    def test_starts_with():
        """Checks that the string starts with the expected prefix."""
        expectation = StringExpectation("hello world")

        expectation.starts_with("hello")

    @staticmethod
    def test_ends_with():
        """Checks that the string ends with the expected suffix."""
        expectation = StringExpectation("hello world")

        expectation.ends_with("world")

    @staticmethod
    def test_is_empty():
        """Checks that the string is empty."""
        expectation = StringExpectation("")

        expectation.is_empty()

    @staticmethod
    def test_has_length():
        """Checks that the string has the expected length."""
        expectation = StringExpectation("hello")

        expectation.has_length(5)

    @staticmethod
    def test_matches():
        """Checks that the string matches the expected regular expression."""
        expectation = StringExpectation("user-123")

        expectation.matches(r"user-\d+")

    def test_starts_with_raises_assertion_error(self):
        """Checks that starts_with() raises for an invalid prefix."""
        expectation = StringExpectation("hello world")

        with self.assertRaises(AssertionError):
            expectation.starts_with("world")

    def test_ends_with_raises_assertion_error(self):
        """Checks that ends_with() raises for an invalid suffix."""
        expectation = StringExpectation("hello world")

        with self.assertRaises(AssertionError):
            expectation.ends_with("hello")

    def test_matches_raises_assertion_error(self):
        """Checks that matches() raises when the pattern does not match."""
        expectation = StringExpectation("user-123")

        with self.assertRaises(AssertionError):
            expectation.matches(r"admin-\d+")