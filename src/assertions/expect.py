from collections.abc import Collection, Mapping
from decimal import Decimal
from typing import Any, overload

import httpx

from src.assertions.boolean import BooleanExpectation
from src.assertions.collection import CollectionExpectation
from src.assertions.http import HttpResponseExpectation
from src.assertions.mapping import MappingExpectation
from src.assertions.numeric import NumericExpectation
from src.assertions.string import StringExpectation
from src.assertions.value import ValueExpectation


@overload
def expect(actual: bool) -> BooleanExpectation: ...


@overload
def expect(actual: str) -> StringExpectation: ...


@overload
def expect(actual: int) -> NumericExpectation[int]: ...


@overload
def expect(actual: float) -> NumericExpectation[float]: ...


@overload
def expect(actual: Decimal) -> NumericExpectation[Decimal]: ...


@overload
def expect(actual: httpx.Response) -> HttpResponseExpectation: ...


@overload
def expect(
    actual: Mapping[Any, Any],
) -> MappingExpectation[Any, Any]: ...


@overload
def expect(
    actual: Collection[Any],
) -> CollectionExpectation[Any]: ...


@overload
def expect(actual: Any) -> ValueExpectation[Any]: ...


def expect(actual: Any):
    if isinstance(actual, bool):
        return BooleanExpectation(actual)

    if isinstance(actual, str):
        return StringExpectation(actual)

    if isinstance(actual, (int, float, Decimal)):
        return NumericExpectation(actual)

    if isinstance(actual, httpx.Response):
        return HttpResponseExpectation(actual)

    if isinstance(actual, Mapping):
        return MappingExpectation(actual)

    if isinstance(actual, Collection):
        return CollectionExpectation(actual)

    return ValueExpectation(actual)
