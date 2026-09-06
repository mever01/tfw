from typing import Generic, TypeVar, Never, Any, Self

T = TypeVar("T")
ExpectationT = TypeVar(
    "ExpectationT",
    bound="BaseExpectation",
)


class BaseExpectation(Generic[T]):
    def __init__(
        self,
        actual: T,
    ):
        self.actual = actual
        self._negated: bool = False

    def _fail(self, message: str) -> Never:
        raise AssertionError(message)

    def _fail_expected(self, expected: Any) -> Never:
        raise AssertionError(
            f"Expected:\n{expected!r}\n\n"
            f"Actual:\n{self.actual!r}"
        )

    @property
    def not_(self: ExpectationT) -> ExpectationT:
        self._negated = True
        return self

    def _assert(
        self,
        condition: bool,
        *,
        expectation: str,
        negated_expectation: str,
    ):
        try:
            if self._negated:
                if condition:
                    self._fail(
                        f"Expected {self.actual!r} {negated_expectation}"
                    )
            elif not condition:
                self._fail(
                    f"Expected {self.actual!r} {expectation}"
                )
        finally:
            self._negated = False
