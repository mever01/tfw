import json
import unittest
from datetime import datetime
from unittest.mock import Mock, patch

import allure

from src.reporting.allure import AllureReporter


class AllureReporterTests(unittest.TestCase):

    @patch("src.reporting.allure.allure.step")
    def test_step_delegates_to_allure(self, step_mock):
        """Checks that step() delegates to Allure."""
        reporter = AllureReporter()
        context_manager = Mock()
        step_mock.return_value = context_manager

        result = reporter.step("Create booking")

        step_mock.assert_called_once_with("Create booking")
        self.assertIs(
            result,
            context_manager,
        )

    @patch("src.reporting.allure.allure.attach")
    def test_attach_text_delegates_to_allure(self, attach_mock):
        """Checks that text attachment is delegated to Allure."""
        reporter = AllureReporter()

        reporter.attach_text(
            "Response",
            "hello",
        )

        attach_mock.assert_called_once_with(
            "hello",
            name="Response",
            attachment_type=allure.attachment_type.TEXT,
        )

    @patch("src.reporting.allure.allure.attach")
    def test_attach_json_serializes_content(self, attach_mock):
        """Checks that JSON content is serialized before attaching."""
        reporter = AllureReporter()
        payload = {
            "id": 1,
            "name": "John",
        }

        reporter.attach_json(
            "Response",
            payload,
        )

        attach_mock.assert_called_once()

        content = attach_mock.call_args.args[0]

        self.assertEqual(
            json.loads(content),
            payload,
        )

    @patch("src.reporting.allure.allure.attach")
    def test_attach_json_uses_expected_allure_metadata(self, attach_mock):
        """Checks that JSON attachment uses the expected Allure metadata."""
        reporter = AllureReporter()

        reporter.attach_json(
            "Response",
            {
                "id": 1,
            },
        )

        kwargs = attach_mock.call_args.kwargs

        self.assertEqual(
            kwargs["name"],
            "Response",
        )
        self.assertEqual(
            kwargs["attachment_type"],
            allure.attachment_type.JSON,
        )

    @patch("src.reporting.allure.allure.attach")
    def test_attach_json_preserves_unicode(self, attach_mock):
        """Checks that JSON serialization preserves readable Unicode."""
        reporter = AllureReporter()

        reporter.attach_json(
            "Response",
            {
                "message": "Привет",
            },
        )

        content = attach_mock.call_args.args[0]

        self.assertIn(
            "Привет",
            content,
        )

    @patch("src.reporting.allure.allure.attach")
    def test_attach_json_formats_content(self, attach_mock):
        """Checks that JSON content is formatted for readability."""
        reporter = AllureReporter()

        reporter.attach_json(
            "Response",
            {
                "id": 1,
            },
        )

        content = attach_mock.call_args.args[0]

        self.assertIn(
            '\n  "id": 1\n',
            content,
        )

    @patch("src.reporting.allure.allure.attach")
    def test_attach_json_serializes_unsupported_types(self, attach_mock):
        """Checks that unsupported JSON types are converted to strings."""
        reporter = AllureReporter()
        created_at = datetime(2026,9,5,12,30,)

        reporter.attach_json(
            "Response",
            {
                "created_at": created_at,
            },
        )

        content = attach_mock.call_args.args[0]

        self.assertEqual(
            json.loads(content),
            {
                "created_at": "2026-09-05 12:30:00",
            },
        )
