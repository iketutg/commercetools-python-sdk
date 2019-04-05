# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._base import PagedQueryResponse, Update, UpdateAction
from commercetools.types._common import Reference, ReferenceTypeId, Resource

if typing.TYPE_CHECKING:
    from ._common import ResourceIdentifier
    from ._customer import CustomerReference
    from ._product import ProductReference
    from ._state import StateReference
    from ._type import CustomFields, CustomFieldsDraft, FieldContainer, TypeReference
__all__ = [
    "Review",
    "ReviewDraft",
    "ReviewPagedQueryResponse",
    "ReviewRatingStatistics",
    "ReviewReference",
    "ReviewSetAuthorNameAction",
    "ReviewSetCustomFieldAction",
    "ReviewSetCustomTypeAction",
    "ReviewSetCustomerAction",
    "ReviewSetKeyAction",
    "ReviewSetLocaleAction",
    "ReviewSetRatingAction",
    "ReviewSetTargetAction",
    "ReviewSetTextAction",
    "ReviewSetTitleAction",
    "ReviewTransitionStateAction",
    "ReviewUpdate",
    "ReviewUpdateAction",
]


class Review(Resource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``uniquenessValue`` `in Commercetools)`
    uniqueness_value: typing.Optional[str]
    #: Optional :class:`str`
    locale: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``authorName`` `in Commercetools)`
    author_name: typing.Optional[str]
    #: Optional :class:`str`
    title: typing.Optional[str]
    #: Optional :class:`str`
    text: typing.Optional[str]
    #: Optional :class:`commercetools.types.ProductReference`
    target: typing.Optional["ProductReference"]
    #: :class:`bool` `(Named` ``includedInStatistics`` `in Commercetools)`
    included_in_statistics: typing.Optional[bool]
    #: Optional :class:`float`
    rating: typing.Optional[float]
    #: Optional :class:`commercetools.types.StateReference`
    state: typing.Optional["StateReference"]
    #: Optional :class:`commercetools.types.CustomerReference`
    customer: typing.Optional["CustomerReference"]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        key: typing.Optional[str] = None,
        uniqueness_value: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        author_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        target: typing.Optional["ProductReference"] = None,
        included_in_statistics: typing.Optional[bool] = None,
        rating: typing.Optional[float] = None,
        state: typing.Optional["StateReference"] = None,
        customer: typing.Optional["CustomerReference"] = None,
        custom: typing.Optional["CustomFields"] = None
    ) -> None:
        self.key = key
        self.uniqueness_value = uniqueness_value
        self.locale = locale
        self.author_name = author_name
        self.title = title
        self.text = text
        self.target = target
        self.included_in_statistics = included_in_statistics
        self.rating = rating
        self.state = state
        self.customer = customer
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "Review(id=%r, version=%r, created_at=%r, last_modified_at=%r, key=%r, uniqueness_value=%r, locale=%r, author_name=%r, title=%r, text=%r, target=%r, included_in_statistics=%r, rating=%r, state=%r, customer=%r, custom=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.key,
                self.uniqueness_value,
                self.locale,
                self.author_name,
                self.title,
                self.text,
                self.target,
                self.included_in_statistics,
                self.rating,
                self.state,
                self.customer,
                self.custom,
            )
        )


class ReviewDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewDraftSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``uniquenessValue`` `in Commercetools)`
    uniqueness_value: typing.Optional[str]
    #: Optional :class:`str`
    locale: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``authorName`` `in Commercetools)`
    author_name: typing.Optional[str]
    #: Optional :class:`str`
    title: typing.Optional[str]
    #: Optional :class:`str`
    text: typing.Optional[str]
    #: Optional :class:`commercetools.types.ProductReference`
    target: typing.Optional["ProductReference"]
    #: Optional :class:`commercetools.types.ResourceIdentifier`
    state: typing.Optional["ResourceIdentifier"]
    #: Optional :class:`float`
    rating: typing.Optional[float]
    #: Optional :class:`commercetools.types.CustomerReference`
    customer: typing.Optional["CustomerReference"]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        uniqueness_value: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        author_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        target: typing.Optional["ProductReference"] = None,
        state: typing.Optional["ResourceIdentifier"] = None,
        rating: typing.Optional[float] = None,
        customer: typing.Optional["CustomerReference"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ) -> None:
        self.key = key
        self.uniqueness_value = uniqueness_value
        self.locale = locale
        self.author_name = author_name
        self.title = title
        self.text = text
        self.target = target
        self.state = state
        self.rating = rating
        self.customer = customer
        self.custom = custom
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ReviewDraft(key=%r, uniqueness_value=%r, locale=%r, author_name=%r, title=%r, text=%r, target=%r, state=%r, rating=%r, customer=%r, custom=%r)"
            % (
                self.key,
                self.uniqueness_value,
                self.locale,
                self.author_name,
                self.title,
                self.text,
                self.target,
                self.state,
                self.rating,
                self.customer,
                self.custom,
            )
        )


class ReviewPagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewPagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.Review`
    results: typing.Optional[typing.Sequence["Review"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Review"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return "ReviewPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)" % (
            self.count,
            self.total,
            self.offset,
            self.results,
        )


class ReviewRatingStatistics(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewRatingStatisticsSchema`."
    #: :class:`int` `(Named` ``averageRating`` `in Commercetools)`
    average_rating: typing.Optional[int]
    #: :class:`int` `(Named` ``highestRating`` `in Commercetools)`
    highest_rating: typing.Optional[int]
    #: :class:`int` `(Named` ``lowestRating`` `in Commercetools)`
    lowest_rating: typing.Optional[int]
    #: :class:`int`
    count: typing.Optional[int]
    #: :class:`object` `(Named` ``ratingsDistribution`` `in Commercetools)`
    ratings_distribution: typing.Optional[object]

    def __init__(
        self,
        *,
        average_rating: typing.Optional[int] = None,
        highest_rating: typing.Optional[int] = None,
        lowest_rating: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        ratings_distribution: typing.Optional[object] = None
    ) -> None:
        self.average_rating = average_rating
        self.highest_rating = highest_rating
        self.lowest_rating = lowest_rating
        self.count = count
        self.ratings_distribution = ratings_distribution
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ReviewRatingStatistics(average_rating=%r, highest_rating=%r, lowest_rating=%r, count=%r, ratings_distribution=%r)"
            % (
                self.average_rating,
                self.highest_rating,
                self.lowest_rating,
                self.count,
                self.ratings_distribution,
            )
        )


class ReviewReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewReferenceSchema`."
    #: Optional :class:`commercetools.types.Review`
    obj: typing.Optional["Review"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        obj: typing.Optional["Review"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.REVIEW, id=id, key=key)

    def __repr__(self) -> str:
        return "ReviewReference(type_id=%r, id=%r, key=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.key,
            self.obj,
        )


class ReviewUpdate(Update):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewUpdateSchema`."
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
        return "ReviewUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class ReviewUpdateAction(UpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewUpdateActionSchema`."

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        super().__init__(action=action)

    def __repr__(self) -> str:
        return "ReviewUpdateAction(action=%r)" % (self.action,)


class ReviewSetAuthorNameAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetAuthorNameActionSchema`."
    #: Optional :class:`str` `(Named` ``authorName`` `in Commercetools)`
    author_name: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        author_name: typing.Optional[str] = None
    ) -> None:
        self.author_name = author_name
        super().__init__(action="setAuthorName")

    def __repr__(self) -> str:
        return "ReviewSetAuthorNameAction(action=%r, author_name=%r)" % (
            self.action,
            self.author_name,
        )


class ReviewSetCustomFieldAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetCustomFieldActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        value: typing.Optional[typing.Any] = None
    ) -> None:
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    def __repr__(self) -> str:
        return "ReviewSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


class ReviewSetCustomTypeAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetCustomTypeActionSchema`."
    #: Optional :class:`commercetools.types.TypeReference`
    type: typing.Optional["TypeReference"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        type: typing.Optional["TypeReference"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    def __repr__(self) -> str:
        return "ReviewSetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


class ReviewSetCustomerAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetCustomerActionSchema`."
    #: Optional :class:`commercetools.types.CustomerReference`
    customer: typing.Optional["CustomerReference"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        customer: typing.Optional["CustomerReference"] = None
    ) -> None:
        self.customer = customer
        super().__init__(action="setCustomer")

    def __repr__(self) -> str:
        return "ReviewSetCustomerAction(action=%r, customer=%r)" % (
            self.action,
            self.customer,
        )


class ReviewSetKeyAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "ReviewSetKeyAction(action=%r, key=%r)" % (self.action, self.key)


class ReviewSetLocaleAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetLocaleActionSchema`."
    #: Optional :class:`str`
    locale: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        locale: typing.Optional[str] = None
    ) -> None:
        self.locale = locale
        super().__init__(action="setLocale")

    def __repr__(self) -> str:
        return "ReviewSetLocaleAction(action=%r, locale=%r)" % (
            self.action,
            self.locale,
        )


class ReviewSetRatingAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetRatingActionSchema`."
    #: Optional :class:`int`
    rating: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        rating: typing.Optional[int] = None
    ) -> None:
        self.rating = rating
        super().__init__(action="setRating")

    def __repr__(self) -> str:
        return "ReviewSetRatingAction(action=%r, rating=%r)" % (
            self.action,
            self.rating,
        )


class ReviewSetTargetAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetTargetActionSchema`."
    #: Optional :class:`commercetools.types.ProductReference`
    target: typing.Optional["ProductReference"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        target: typing.Optional["ProductReference"] = None
    ) -> None:
        self.target = target
        super().__init__(action="setTarget")

    def __repr__(self) -> str:
        return "ReviewSetTargetAction(action=%r, target=%r)" % (
            self.action,
            self.target,
        )


class ReviewSetTextAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetTextActionSchema`."
    #: Optional :class:`str`
    text: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, text: typing.Optional[str] = None
    ) -> None:
        self.text = text
        super().__init__(action="setText")

    def __repr__(self) -> str:
        return "ReviewSetTextAction(action=%r, text=%r)" % (self.action, self.text)


class ReviewSetTitleAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewSetTitleActionSchema`."
    #: Optional :class:`str`
    title: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, title: typing.Optional[str] = None
    ) -> None:
        self.title = title
        super().__init__(action="setTitle")

    def __repr__(self) -> str:
        return "ReviewSetTitleAction(action=%r, title=%r)" % (self.action, self.title)


class ReviewTransitionStateAction(ReviewUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReviewTransitionStateActionSchema`."
    #: :class:`commercetools.types.StateReference`
    state: typing.Optional["StateReference"]
    #: Optional :class:`bool`
    force: typing.Optional[bool]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        state: typing.Optional["StateReference"] = None,
        force: typing.Optional[bool] = None
    ) -> None:
        self.state = state
        self.force = force
        super().__init__(action="transitionState")

    def __repr__(self) -> str:
        return "ReviewTransitionStateAction(action=%r, state=%r, force=%r)" % (
            self.action,
            self.state,
            self.force,
        )