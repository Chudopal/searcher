from typing import List, Dict
from domain.models import Model
from domain.interfaces import (
    DatabaseManagerInterface,
)


class DatabaseManager(DatabaseManagerInterface):

    def get(
        self, model: type, **where_params
    ) -> List[Model]:
        self.database_connection.connect()
        query = self.query_creator.get_query(
            model, **where_params
        )
        self.database_connection.execute(query)
        result = self._prepare_result(model,
            self.database_connection.get())
        self.database_connection.close()
        return result

    def update(
        self, model: Model, data, **where_params
    ) -> None:
        self.database_connection.connect()
        query = self.query_creator.update_query(
            model, data, **where_params
        )
        self._execute(query)

    def create(
        self, model: type, data: List[Model]
    ) -> None:
        self.database_connection.connect()
        query = self.query_creator.create_query(
            model, [dict(data_item) for data_item in data]
        )
        self._execute(query)

    def delete(
        self, model: type, **where_params
    ) -> None:
        self.database_connection.connect()
        query = self.query_creator.delete_query(
            model, **where_params
        )
        self._execute(query)

    def _execute(self, query):
        self.database_connection.execute(query)
        self.database_connection.commit()
        self.database_connection.close()

    def _prepare_result(
        self, model: type, result: Dict
    ) -> List[Model]:
        return [model(**row) for row in result]

