# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._base import PagedQueryResponse, Update, UpdateAction
from commercetools.types._common import Reference, ReferenceTypeId, Resource

if typing.TYPE_CHECKING:
    from ._common import LocalizedString
__all__ = [
    "State",
    "StateAddRolesAction",
    "StateChangeInitialAction",
    "StateChangeKeyAction",
    "StateChangeTypeAction",
    "StateDraft",
    "StatePagedQueryResponse",
    "StateReference",
    "StateRemoveRolesAction",
    "StateRoleEnum",
    "StateSetDescriptionAction",
    "StateSetNameAction",
    "StateSetRolesAction",
    "StateSetTransitionsAction",
    "StateTypeEnum",
    "StateUpdate",
    "StateUpdateAction",
]


class State(Resource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.StateTypeEnum`
    type: typing.Optional["StateTypeEnum"]
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`bool`
    initial: typing.Optional[bool]
    #: :class:`bool` `(Named` ``builtIn`` `in Commercetools)`
    built_in: typing.Optional[bool]
    #: Optional list of :class:`commercetools.types.StateRoleEnum`
    roles: typing.Optional[typing.List["StateRoleEnum"]]
    #: Optional list of :class:`commercetools.types.StateReference`
    transitions: typing.Optional[typing.List["StateReference"]]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        key: typing.Optional[str] = None,
        type: typing.Optional["StateTypeEnum"] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        initial: typing.Optional[bool] = None,
        built_in: typing.Optional[bool] = None,
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None,
        transitions: typing.Optional[typing.List["StateReference"]] = None
    ) -> None:
        self.key = key
        self.type = type
        self.name = name
        self.description = description
        self.initial = initial
        self.built_in = built_in
        self.roles = roles
        self.transitions = transitions
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "State(id=%r, version=%r, created_at=%r, last_modified_at=%r, key=%r, type=%r, name=%r, description=%r, initial=%r, built_in=%r, roles=%r, transitions=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.key,
                self.type,
                self.name,
                self.description,
                self.initial,
                self.built_in,
                self.roles,
                self.transitions,
            )
        )


class StateDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateDraftSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.StateTypeEnum`
    type: typing.Optional["StateTypeEnum"]
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: Optional :class:`bool`
    initial: typing.Optional[bool]
    #: Optional list of :class:`commercetools.types.StateRoleEnum`
    roles: typing.Optional[typing.List["StateRoleEnum"]]
    #: Optional list of :class:`commercetools.types.StateReference`
    transitions: typing.Optional[typing.List["StateReference"]]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        type: typing.Optional["StateTypeEnum"] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        initial: typing.Optional[bool] = None,
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None,
        transitions: typing.Optional[typing.List["StateReference"]] = None
    ) -> None:
        self.key = key
        self.type = type
        self.name = name
        self.description = description
        self.initial = initial
        self.roles = roles
        self.transitions = transitions
        super().__init__()

    def __repr__(self) -> str:
        return (
            "StateDraft(key=%r, type=%r, name=%r, description=%r, initial=%r, roles=%r, transitions=%r)"
            % (
                self.key,
                self.type,
                self.name,
                self.description,
                self.initial,
                self.roles,
                self.transitions,
            )
        )


class StatePagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StatePagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.State`
    results: typing.Optional[typing.Sequence["State"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["State"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return "StatePagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)" % (
            self.count,
            self.total,
            self.offset,
            self.results,
        )


class StateReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateReferenceSchema`."
    #: Optional :class:`commercetools.types.State`
    obj: typing.Optional["State"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        obj: typing.Optional["State"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.STATE, id=id, key=key)

    def __repr__(self) -> str:
        return "StateReference(type_id=%r, id=%r, key=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.key,
            self.obj,
        )


class StateRoleEnum(enum.Enum):
    REVIEW_INCLUDED_IN_STATISTICS = "ReviewIncludedInStatistics"


class StateTypeEnum(enum.Enum):
    ORDER_STATE = "OrderState"
    LINE_ITEM_STATE = "LineItemState"
    PRODUCT_STATE = "ProductState"
    REVIEW_STATE = "ReviewState"
    PAYMENT_STATE = "PaymentState"


class StateUpdate(Update):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateUpdateSchema`."
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.actions = actions
        super().__init__(version=version, actions=actions)

    def __repr__(self) -> str:
        return "StateUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class StateUpdateAction(UpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateUpdateActionSchema`."

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        super().__init__(action=action)

    def __repr__(self) -> str:
        return "StateUpdateAction(action=%r)" % (self.action,)


class StateAddRolesAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateAddRolesActionSchema`."
    #: List of :class:`commercetools.types.StateRoleEnum`
    roles: typing.Optional[typing.List["StateRoleEnum"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None
    ) -> None:
        self.roles = roles
        super().__init__(action="addRoles")

    def __repr__(self) -> str:
        return "StateAddRolesAction(action=%r, roles=%r)" % (self.action, self.roles)


class StateChangeInitialAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateChangeInitialActionSchema`."
    #: :class:`bool`
    initial: typing.Optional[bool]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        initial: typing.Optional[bool] = None
    ) -> None:
        self.initial = initial
        super().__init__(action="changeInitial")

    def __repr__(self) -> str:
        return "StateChangeInitialAction(action=%r, initial=%r)" % (
            self.action,
            self.initial,
        )


class StateChangeKeyAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateChangeKeyActionSchema`."
    #: :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="changeKey")

    def __repr__(self) -> str:
        return "StateChangeKeyAction(action=%r, key=%r)" % (self.action, self.key)


class StateChangeTypeAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateChangeTypeActionSchema`."
    #: :class:`commercetools.types.StateTypeEnum`
    type: typing.Optional["StateTypeEnum"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        type: typing.Optional["StateTypeEnum"] = None
    ) -> None:
        self.type = type
        super().__init__(action="changeType")

    def __repr__(self) -> str:
        return "StateChangeTypeAction(action=%r, type=%r)" % (self.action, self.type)


class StateRemoveRolesAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateRemoveRolesActionSchema`."
    #: List of :class:`commercetools.types.StateRoleEnum`
    roles: typing.Optional[typing.List["StateRoleEnum"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None
    ) -> None:
        self.roles = roles
        super().__init__(action="removeRoles")

    def __repr__(self) -> str:
        return "StateRemoveRolesAction(action=%r, roles=%r)" % (self.action, self.roles)


class StateSetDescriptionAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateSetDescriptionActionSchema`."
    #: :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "StateSetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class StateSetNameAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateSetNameActionSchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.name = name
        super().__init__(action="setName")

    def __repr__(self) -> str:
        return "StateSetNameAction(action=%r, name=%r)" % (self.action, self.name)


class StateSetRolesAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateSetRolesActionSchema`."
    #: List of :class:`commercetools.types.StateRoleEnum`
    roles: typing.Optional[typing.List["StateRoleEnum"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None
    ) -> None:
        self.roles = roles
        super().__init__(action="setRoles")

    def __repr__(self) -> str:
        return "StateSetRolesAction(action=%r, roles=%r)" % (self.action, self.roles)


class StateSetTransitionsAction(StateUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StateSetTransitionsActionSchema`."
    #: Optional list of :class:`commercetools.types.StateReference`
    transitions: typing.Optional[typing.List["StateReference"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transitions: typing.Optional[typing.List["StateReference"]] = None
    ) -> None:
        self.transitions = transitions
        super().__init__(action="setTransitions")

    def __repr__(self) -> str:
        return "StateSetTransitionsAction(action=%r, transitions=%r)" % (
            self.action,
            self.transitions,
        )
