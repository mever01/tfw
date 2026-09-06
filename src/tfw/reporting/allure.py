import json

import allure


class AllureReporter:

    # Instance method intentionally kept to satisfy the Reporter contract.
    # noinspection PyMethodMayBeStatic
    def step(self, name: str):
        return allure.step(name)

    # noinspection PyMethodMayBeStatic
    def attach_text(
        self,
        name: str,
        content: str,
    ):
        allure.attach(
            content,
            name=name,
            attachment_type=allure.attachment_type.TEXT,
        )

    # noinspection PyMethodMayBeStatic
    def attach_json(
        self,
        name: str,
        content,
    ):
        allure.attach(
            json.dumps(
                content,
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
            name=name,
            attachment_type=allure.attachment_type.JSON,
        )
