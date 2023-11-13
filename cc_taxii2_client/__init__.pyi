"""__init__.pyi"""

from __future__ import annotations
from typing import Generator
from abc import ABC
from requests.models import Response


class TaxiiError(Exception):
    ...


class TaxiiCollectionError(TaxiiError):
    ...


class TaxiiConnectionError(TaxiiError):
    ...


class TaxiiAuthorizationError(TaxiiError):
    ...


class TaxiiDatetimeError(TaxiiError):
    ...


class TaxiiFilterError(TaxiiError):
    ...


class Stix2ObjectBase(ABC):
    ...


class EnvelopeBase(ABC):
    ...


class CCIndicator(Stix2ObjectBase):
    created: str
    description: str
    id: str
    modified: str
    name: str
    pattern: str
    pattern_type: str
    pattern_version: str
    spec_version: str
    type: str
    valid_from: str


class Envelope(EnvelopeBase):
    objects: list[dict[str, str]] | None
    more: bool | None
    next: str | None


class TaxiiClient(ABC):

    def __init__(self, account: str, api_key: str) -> None:
        ...

    def get_collections(self, root: str) -> list[str]:
        ...

    def _taxii_request(self, root: str, collection_id: str,
                       parameters: str) -> Response:
        ...

    def _get_json(self, root: str, collection_id: str,
                  parameters: str) -> EnvelopeBase:
        ...

    def get_stix2_objects(self, root: str, collection_id: str | None,
                          limit: int, added_after: str | None,
                          match: dict[str, str] | None,
                          follow_pages: bool) -> list[Stix2ObjectBase]:
        ...


class CCTaxiiClient(TaxiiClient):

    def get_cc_indicators_generator(
        self,
        collection_id: str | None = None,
        limit: int = 1000,
        private: bool = False,
        added_after: str | None = None,
        match: dict[str, str] | None = None,
        follow_pages: bool = False
    ) -> Generator[list[CCIndicator], None, None]:
        ...


def _search(
        field: str, keyword: str,
        indicators: Generator[list[CCIndicator], None,
                              None]) -> list[CCIndicator]:
    ...


def count_indicators(
        indicators: Generator[list[CCIndicator], None, None]) -> int:
    ...


def ip_search(
        ip_address: str, indicators: Generator[list[CCIndicator], None,
                                               None]) -> list[CCIndicator]:
    ...


def description_search(
        description: str, indicators: Generator[list[CCIndicator], None,
                                                None]) -> list[CCIndicator]:
    ...
