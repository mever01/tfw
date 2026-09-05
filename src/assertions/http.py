import httpx

from src.assertions.base import BaseExpectation


class HttpResponseExpectation(BaseExpectation[httpx.Response]):

    def status(self, expected: int):
        self._assert(
            self.actual.status_code == expected,
            expectation=f"to have status {expected}",
            negated_expectation=f"not to have status {expected}",
        )

    def status_in(self, expected: set[int]):
        self._assert(
            self.actual.status_code in expected,
            expectation=f"to have status in {expected!r}",
            negated_expectation=f"not to have status in {expected!r}",
        )

    def has_header(self, expected: str):
        self._assert(
            expected in self.actual.headers,
            expectation=f"to have header {expected!r}",
            negated_expectation=f"not to have header {expected!r}",
        )

    def header_equal(
        self,
        header: str,
        expected: str,
    ):
        actual = self.actual.headers.get(header)

        self._assert(
            actual == expected,
            expectation=(
                f"to have header {header!r} "
                f"equal to {expected!r}"
            ),
            negated_expectation=(
                f"not to have header {header!r} "
                f"equal to {expected!r}"
            ),
        )

    def content_type(self, expected: str):
        actual = self.actual.headers.get("content-type")

        self._assert(
            actual is not None
            and actual.split(";", maxsplit=1)[0].strip() == expected,
            expectation=f"to have content type {expected!r}",
            negated_expectation=f"not to have content type {expected!r}",
        )

    def contains_text(self, expected: str):
        self._assert(
            expected in self.actual.text,
            expectation=f"to contain text {expected!r}",
            negated_expectation=f"not to contain text {expected!r}",
        )

    def json_equal(self, expected):
        actual = self.actual.json()

        self._assert(
            actual == expected,
            expectation=f"to have JSON equal to {expected!r}",
            negated_expectation=f"not to have JSON equal to {expected!r}",
        )
