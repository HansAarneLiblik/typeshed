from _typeshed import Incomplete, SupportsKeysAndGetItem
from collections.abc import Callable, Generator, Iterable, Iterator, Mapping
from contextlib import contextmanager
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from ._format import FormatChecker
from ._types import TypeChecker
from ._utils import Unset, URIDict
from .exceptions import ValidationError

# these type aliases do not exist at runtime, they're only defined here in the stub
_JsonObject: TypeAlias = Mapping[str, Any]
_JsonValue: TypeAlias = _JsonObject | list[Any] | str | int | float | bool | None
_ValidatorCallback: TypeAlias = Callable[[Any, Any, _JsonValue, _JsonObject], Iterator[ValidationError]]

_Schema: TypeAlias = Mapping[str, Any]

# This class does not exist at runtime. Compatible classes are created at
# runtime by create().
class _Validator:
    VALIDATORS: ClassVar[dict[Incomplete, Incomplete]]
    META_SCHEMA: ClassVar[dict[Incomplete, Incomplete]]
    TYPE_CHECKER: ClassVar[Incomplete]
    FORMAT_CHECKER: ClassVar[Incomplete]
    @staticmethod
    def ID_OF(schema: _Schema) -> str: ...
    schema: _Schema
    resolver: Incomplete
    format_checker: Incomplete
    evolve: Incomplete
    def __init__(
        self,
        schema: _Schema,
        resolver: Incomplete | None = ...,
        format_checker: Incomplete | None = ...,
        registry: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def check_schema(cls, schema: _Schema, format_checker: FormatChecker | Unset = ...) -> None: ...
    def iter_errors(self, instance, _schema: _Schema | None = ...) -> Generator[Incomplete, None, None]: ...
    def descend(
        self, instance, schema: _Schema, path: Incomplete | None = ..., schema_path: Incomplete | None = ...
    ) -> Generator[Incomplete, None, None]: ...
    def validate(self, *args, **kwargs) -> None: ...
    def is_type(self, instance, type): ...
    def is_valid(self, instance, _schema: _Schema | None = ...) -> bool: ...

def validates(version: str) -> Callable[..., Incomplete]: ...
def create(
    meta_schema: _Schema,
    validators: Mapping[str, _ValidatorCallback] | tuple[()] = (),
    version: Incomplete | None = None,
    type_checker: TypeChecker = ...,
    format_checker: FormatChecker = ...,
    id_of: Callable[[_Schema], str] = ...,
    applicable_validators: Callable[[_Schema], Iterable[tuple[str, _ValidatorCallback]]] = ...,
) -> type[_Validator]: ...
def extend(
    validator,
    validators=(),
    version: Incomplete | None = None,
    type_checker: Incomplete | None = None,
    format_checker: Incomplete | None = None,
): ...

# At runtime these are fields that are assigned the return values of create() calls.
class Draft3Validator(_Validator): ...
class Draft4Validator(_Validator): ...
class Draft6Validator(_Validator): ...
class Draft7Validator(_Validator): ...
class Draft201909Validator(_Validator): ...
class Draft202012Validator(_Validator): ...

_Handler: TypeAlias = Callable[[str], Incomplete]

class RefResolver:
    referrer: dict[str, Incomplete]
    cache_remote: Incomplete
    handlers: dict[str, _Handler]
    store: URIDict
    def __init__(
        self,
        base_uri: str,
        referrer: dict[str, Incomplete],
        store: SupportsKeysAndGetItem[str, str] | Iterable[tuple[str, str]] = ...,
        cache_remote: bool = True,
        handlers: SupportsKeysAndGetItem[str, _Handler] | Iterable[tuple[str, _Handler]] = (),
        urljoin_cache: Incomplete | None = None,
        remote_cache: Incomplete | None = None,
    ) -> None: ...
    @classmethod
    def from_schema(cls, schema: _Schema, id_of=..., *args, **kwargs): ...
    def push_scope(self, scope) -> None: ...
    def pop_scope(self) -> None: ...
    @property
    def resolution_scope(self): ...
    @property
    def base_uri(self): ...
    @contextmanager
    def in_scope(self, scope) -> Generator[None, None, None]: ...
    @contextmanager
    def resolving(self, ref) -> Generator[Incomplete, None, None]: ...
    def resolve(self, ref): ...
    def resolve_from_url(self, url): ...
    def resolve_fragment(self, document, fragment): ...
    def resolve_remote(self, uri): ...

def validate(instance: object, schema: _Schema, cls: type[_Validator] | None = None, *args: Any, **kwargs: Any) -> None: ...
def validator_for(schema: _Schema | bool, default=...): ...
