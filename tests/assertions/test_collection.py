import unittest

from tfw.assertions.collection import CollectionExpectation


class CollectionExpectationTests(unittest.TestCase):

    @staticmethod
    def test_contains():
        """Checks that the collection contains the expected item."""
        expectation = CollectionExpectation([1, 2, 3])

        expectation.contains(2)

    @staticmethod
    def test_contains_all():
        """Checks that the collection contains all expected items."""
        expectation = CollectionExpectation([1, 2, 3])

        expectation.contains_all([1, 3])

    @staticmethod
    def test_has_length():
        """Checks that the collection has the expected length."""
        expectation = CollectionExpectation([1, 2, 3])

        expectation.has_length(3)

    @staticmethod
    def test_is_empty():
        """Checks that the collection is empty."""
        expectation = CollectionExpectation([])

        expectation.is_empty()

    @staticmethod
    def test_not_contains():
        """Checks successful negated item containment assertion."""
        expectation = CollectionExpectation([1, 2, 3])

        expectation.not_.contains(4)

    def test_contains_all_raises_when_item_is_missing(self):
        """Checks that contains_all() raises when an expected item is missing."""
        expectation = CollectionExpectation([1, 2, 3])

        with self.assertRaises(AssertionError):
            expectation.contains_all([1, 4])
