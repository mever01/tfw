import unittest

from tfw.assertions.mapping import MappingExpectation


class MappingExpectationTests(unittest.TestCase):

    def setUp(self):
        self.payload = {
            "id": 1,
            "status": "active",
            "name": "John",
        }

    def test_has_key(self):
        """Checks that the mapping contains the expected key."""
        expectation = MappingExpectation(self.payload)

        expectation.has_key("id")

    def test_has_keys(self):
        """Checks that the mapping contains all expected keys."""
        expectation = MappingExpectation(self.payload)

        expectation.has_keys(
            {"id", "status"}
        )

    def test_has_value(self):
        """Checks that the mapping contains the expected value."""
        expectation = MappingExpectation(self.payload)

        expectation.has_value("active")

    def test_contains_item(self):
        """Checks that the mapping contains the expected key-value pair."""
        expectation = MappingExpectation(self.payload)

        expectation.contains_item(
            "status",
            "active",
        )

    def test_has_length(self):
        """Checks that the mapping has the expected length."""
        expectation = MappingExpectation(self.payload)

        expectation.has_length(3)

    @staticmethod
    def test_is_empty():
        """Checks that the mapping is empty."""
        expectation = MappingExpectation({})

        expectation.is_empty()

    def test_contains_item_raises_for_wrong_value(self):
        """Checks that contains_item() raises when the value does not match."""
        expectation = MappingExpectation(self.payload)

        with self.assertRaises(AssertionError):
            expectation.contains_item(
                "status",
                "inactive",
            )

    def test_has_keys_raises_when_key_is_missing(self):
        """Checks that has_keys() raises when an expected key is missing."""
        expectation = MappingExpectation(self.payload)

        with self.assertRaises(AssertionError):
            expectation.has_keys(
                {"id", "unknown"}
            )
