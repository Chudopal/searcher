from typing import Dict, List
from domain.interfaces import ModelMapperInterface
from infrastructure.database.queries import (
    CreateDocumentQuery,
    CreateWordQuery,
    UpdateDocumentQuery,
    UpdateWordQuery,
    GetDocumentQuery,
    GetWordQuery,
    GetWordDocumentAssotiationQuery,
    CountDocumentQuery,
    CountWordDocumentAssotiationQuery,
    CountWordQuery,
    DeleteDocumentQuery,
    DeleteWordQuery,
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
        return super().update(data, **where_params)

    def create(self, data: List[Dict]) -> str:
        return super().create(data)

    def count(self, **where_params) -> str:
        return CountWordDocumentAssotiationQuery(**where_params).build()