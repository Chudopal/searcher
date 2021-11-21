from typing import Dict, List

from domain.interfaces import QueryFactory

from domain.models import Word
from domain.models import Document
from domain.models import WordDocumentAssotiation

from infrastructure.database.model_database_mapper import WordMapper
from infrastructure.database.model_database_mapper import DocumentMapper
from infrastructure.database.model_database_mapper import WordDocumentAssotiationMapper


class QueryCreator(QueryFactory):

    table_names_mapper: Dict[type, type] = {
        Word: WordMapper,
        Document: DocumentMapper,
        WordDocumentAssotiation: WordDocumentAssotiationMapper,
    }

    def __init__(self, model_mapper: Dict = None):
        self.table_names_mapper.update(
            model_mapper if model_mapper else {}
        )

    def get_query(
        self, model: type, **where_params
    ) -> str:
        return self.table_names_mapper.get(
            model
        )().get(**where_params)

    def create_query(
        self, model: type, data: List[Dict]
    ) -> str:
        return self.table_names_mapper.get(
            model
        )().create(data)

    def update_query(
        self, model: type, data: Dict, **where_params
    ) -> str:
        return self.table_names_mapper.get(
            model
        )().update(data, **where_params)

    def delete_query(
        self, model: type, **where_params
    ) -> str:
        return self.table_names_mapper.get(
            model
        )().delete(**where_params)

    def count_query(self, model: type, **where_params) -> str:
        return self.table_names_mapper.get(
            model
        )().count(**where_params)