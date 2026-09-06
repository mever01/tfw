import unittest
from decimal import Decimal

import httpx

from tfw.assertions.boolean import BooleanExpectation
from tfw.assertions.collection import CollectionExpectation
from tfw.assertions.expect import expect
from tfw.assertions.http import HttpResponseExpectation
from tfw.assertions.mapping import MappingExpectation
from tfw.assertions.numeric import NumericExpectation
from tfw.assertions.string import StringExpectation
from tfw.assertions.value import ValueExpectation


class ExpectDispatcherTests(unittest.TestCase):

    def test_boolean(self):
        """Checks that bool values are dispatched to BooleanExpectation."""
        self.assertIsInstance(
            expect(True),
            BooleanExpectation,
        )

    def test_string(self):
        """Checks that string values are dispatched to StringExpectation."""
        self.assertIsInstance(
            expect("hello"),
            StringExpectation,
        )

    def test_integer(self):
        """Checks that integer values are dispatched to NumericExpectation."""
        self.assertIsInstance(
            expect(10),
            NumericExpectation,
        )

    def test_float(self):
        """Checks that float values are dispatched to NumericExpectation."""
        self.assertIsInstance(
            expect(10.5),
            NumericExpectation,
        )

    def test_decimal(self):
        """Checks that Decimal values are dispatched to NumericExpectation."""
        self.assertIsInstance(
            expect(Decimal("10.5")),
            NumericExpectation,
        )

    def test_mapping(self):
        """Checks that mapping values are dispatched to MappingExpectation."""
        self.assertIsInstance(
            expect({"id": 1}),
            MappingExpectation,
        )

    def test_collection(self):
        """Checks that collection values are dispatched to CollectionExpectation."""
        self.assertIsInstance(
            expect([1, 2, 3]),
            CollectionExpectation,
        )

    def test_http_response(self):
        """Checks that HTTP responses are dispatched to HttpResponseExpectation."""
        response = httpx.Response(
            status_code=200
        )

        self.assertIsInstance(
            expect(response),
            HttpResponseExpectation,
        )

    def test_fallback(self):
        """Checks that unsupported types fall back to ValueExpectation."""

        class CustomObject:
            pass

        self.assertIsInstance(
            expect(CustomObject()),
            ValueExpectation,
        )
