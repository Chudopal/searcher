from typing import Dict, List
from domain.interfaces import ModelMapperInterface
from infrastructure.database.queries import (
    CreateDocumentQuery,
    CreateWordQuery,
    UpdateDocumentQuery,
    UpdateWordQuery,
    GetDocumentQuery,
    GetWordQuery,
#    GetWordDocumentAssotiationQuery,
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


class DocumentMapper(ModelMapperInterface):

    def get(self, **where_params) -> str:
        return GetDocumentQuery(**where_params).build()

    def update(self, data: Dict, **where_params) -> str:
        return UpdateDocumentQuery(data, **where_params).build()

    def create(self, data: List[Dict]) -> str:
        return CreateDocumentQuery(data).build()

    def delete(self, **where_params) -> str:
        return DeleteDocumentQuery(**where_params).build()