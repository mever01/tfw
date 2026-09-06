from tfw.assertions.value import ValueExpectation


class BooleanExpectation(ValueExpectation[bool]):

    def is_true(self):
        self._assert(
            self.actual is True,
            expectation="to be True",
            negated_expectation="not to be True",
        )

    def is_false(self):
        self._assert(
            self.actual is False,
            expectation="to be False",
            negated_expectation="not to be False",
        )
