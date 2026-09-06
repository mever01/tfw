from collections.abc import Collection, Mapping
from decimal import Decimal
from typing import Any, overload

import httpx

from tfw.assertions.boolean import BooleanExpectation
from tfw.assertions.collection import CollectionExpectation
from tfw.assertions.http import HttpResponseExpectation
from tfw.assertions.mapping import MappingExpectation
from tfw.assertions.numeric import NumericExpectation
from tfw.assertions.string import StringExpectation
from tfw.assertions.value import ValueExpectation


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
