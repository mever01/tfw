import unittest

from tfw.reporting.null import NullReporter


class NullReporterTests(unittest.TestCase):

    @staticmethod
    def test_step_can_be_used_as_context_manager():
        """Checks that step() can be used as a context manager."""
        reporter = NullReporter()

        with reporter.step("Test step"):
            value = 1

        assert value == 1

    @staticmethod
    def test_attach_text_does_not_raise():
        """Checks that text attachment is safely ignored."""
        reporter = NullReporter()

        reporter.attach_text(
            "Test attachment",
            "hello",
        )

    @staticmethod
    def test_attach_json_does_not_raise():
        """Checks that JSON attachment is safely ignored."""
        reporter = NullReporter()

        reporter.attach_json(
            "Test attachment",
            {
                "id": 1,
            },
        )
