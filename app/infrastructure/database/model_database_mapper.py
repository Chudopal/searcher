from typing import Dict, List
from domain.interfaces import ModelMapperInterface
from infrastructure.database.queries import (
    CreateDocumentQuery,
    CreateWordQuery,
    CreateWordDocumentAssotiationQuery,
    UpdateDocumentQuery,
    UpdateWordQuery,
    UpdateWordDocumentAssotiationQuery,
    GetDocumentQuery,
    GetWordQuery,
    GetWordDocumentAssotiationQuery,
    CountDocumentQuery,
    CountWordDocumentAssotiationQuery,
    CountWordQuery,
    DeleteDocumentQuery,
    DeleteWordQuery,
    DeleteWordDocumentAssotiationQuery
)


class WordMapper(ModelMapperInterface):

    def get(self, **where_params) -> str:
        return GetWordQuery(**where_params).build()

    def update(self, data: Dict, **where_params) -> str:
        return UpdateWordQuery(data, **where_params).build()

    def create(self, data: List[Dict]) -> str:
        return CreateWordQuery(data).build()

    def delete(self, **where_params) -> str:
        return DeleteWordQuery(**where_params).build()

    def count(self, **where_params) -> str:
        return CountWordQuery(**where_params).build()


class DocumentMapper(ModelMapperInterface):

    def get(self, **where_params) -> str:
        return GetDocumentQuery(**where_params).build()

    def update(self, data: Dict, **where_params) -> str:
        return UpdateDocumentQuery(data, **where_params).build()

    def create(self, data: List[Dict]) -> str:
        return CreateDocumentQuery(data).build()

    def delete(self, **where_params) -> str:
        return DeleteDocumentQuery(**where_params).build()

    def count(self, **where_params) -> str:
        return CountDocumentQuery(**where_params).build()


class WordDocumentAssotiationMapper(ModelMapperInterface):

    def get(self, **where_params) -> str:
        return GetWordDocumentAssotiationQuery(**where_params).build()

    def update(self, data: Dict, **where_params) -> str:
        return UpdateWordDocumentAssotiationQuery(data, **where_params).build()

    def create(self, data: List[Dict]) -> str:
        return CreateWordDocumentAssotiationQuery(data).build()

    def delete(self, **where_params) -> str:
        return DeleteWordDocumentAssotiationQuery(**where_params).build()

    def count(self, **where_params) -> str:
        return CountWordDocumentAssotiationQuery(**where_params).build()