import unittest

import httpx

from tfw.assertions.http import HttpResponseExpectation


class HttpResponseExpectationTests(unittest.TestCase):

    @staticmethod
    def test_status():
        """Checks that the response has the expected status code."""
        response = httpx.Response(
            status_code=200,
        )

        expectation = HttpResponseExpectation(response)

        expectation.status(200)

    @staticmethod
    def test_status_in():
        """Checks that the response status code is in the expected collection."""
        response = httpx.Response(
            status_code=201,
        )

        expectation = HttpResponseExpectation(response)

        expectation.status_in(
            {200, 201}
        )

    @staticmethod
    def test_has_header():
        """Checks that the response contains the expected header."""
        response = httpx.Response(
            status_code=200,
            headers={
                "content-type": "application/json",
            },
        )

        expectation = HttpResponseExpectation(response)

        expectation.has_header(
            "content-type"
        )

    @staticmethod
    def test_header_equal():
        """Checks that the response header has the expected value."""
        response = httpx.Response(
            status_code=200,
            headers={
                "x-request-id": "abc-123",
            },
        )

        expectation = HttpResponseExpectation(response)

        expectation.header_equal(
            "x-request-id",
            "abc-123",
        )

    @staticmethod
    def test_content_type():
        """Checks that the response has the expected content type."""
        response = httpx.Response(
            status_code=200,
            headers={
                "content-type":
                    "application/json; charset=utf-8",
            },
        )

        expectation = HttpResponseExpectation(response)

        expectation.content_type(
            "application/json"
        )

    @staticmethod
    def test_contains_text():
        """Checks that the response body contains the expected text."""
        response = httpx.Response(
            status_code=200,
            text="hello world",
        )

        expectation = HttpResponseExpectation(response)

        expectation.contains_text("world")

    @staticmethod
    def test_json_equal():
        """Checks that the response JSON equals the expected payload."""
        response = httpx.Response(
            status_code=200,
            json={
                "id": 1,
                "name": "John",
            },
        )

        expectation = HttpResponseExpectation(response)

        expectation.json_equal(
            {
                "id": 1,
                "name": "John",
            }
        )

    def test_status_raises_for_unexpected_status(self):
        """Checks that status() raises for an unexpected status code."""
        response = httpx.Response(status_code=404)

        expectation = HttpResponseExpectation(response)

        with self.assertRaises(AssertionError):
            expectation.status(200)

    def test_content_type_raises_for_unexpected_content_type(self):
        """Checks that content_type() raises for a different content type."""
        response = httpx.Response(
            status_code=200,
            headers={
                "content-type": "text/html; charset=utf-8",
            },
        )

        expectation = HttpResponseExpectation(response)

        with self.assertRaises(AssertionError):
            expectation.content_type("application/json")
