# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._base import PagedQueryResponse
from commercetools.types._common import Reference, ReferenceTypeId, Resource

__all__ = [
    "CustomObject",
    "CustomObjectDraft",
    "CustomObjectPagedQueryResponse",
    "CustomObjectReference",
]


class CustomObject(Resource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomObjectSchema`."
    #: :class:`str`
    container: typing.Optional[str]
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        container: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        value: typing.Optional[typing.Any] = None
    ) -> None:
        self.container = container
        self.key = key
        self.value = value
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "CustomObject(id=%r, version=%r, created_at=%r, last_modified_at=%r, container=%r, key=%r, value=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.container,
                self.key,
                self.value,
            )
        )


class CustomObjectDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomObjectDraftSchema`."
    #: :class:`str`
    container: typing.Optional[str]
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`typing.Any`
    value: typing.Optional[typing.Any]
    #: Optional :class:`int`
    version: typing.Optional[int]

    def __init__(
        self,
        *,
        container: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        value: typing.Optional[typing.Any] = None,
        version: typing.Optional[int] = None
    ) -> None:
        self.container = container
        self.key = key
        self.value = value
        self.version = version
        super().__init__()

    def __repr__(self) -> str:
        return "CustomObjectDraft(container=%r, key=%r, value=%r, version=%r)" % (
            self.container,
            self.key,
            self.value,
            self.version,
        )


class CustomObjectPagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomObjectPagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.CustomObject`
    results: typing.Optional[typing.Sequence["CustomObject"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["CustomObject"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return (
            "CustomObjectPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


class CustomObjectReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomObjectReferenceSchema`."
    #: Optional :class:`commercetools.types.CustomObject`
    obj: typing.Optional["CustomObject"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        obj: typing.Optional["CustomObject"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.KEY_VALUE_DOCUMENT, id=id, key=key)

    def __repr__(self) -> str:
        return "CustomObjectReference(type_id=%r, id=%r, key=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.key,
            self.obj,
        )
