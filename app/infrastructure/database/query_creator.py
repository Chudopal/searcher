from typing import Dict, List
from domain.interfaces import QueryFactory


class QueryCreator(QueryFactory):

    table_names_mapper: Dict[type, str] = dict()

    def __init__(self, model_mapper: Dict):
        self.table_names_mapper.update(model_mapper)

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