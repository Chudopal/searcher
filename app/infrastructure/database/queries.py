from typing import Dict, List
from domain.interfaces import QueryInterface


class ConditionalQuery(QueryInterface):

    def __init__(self, **where_params):
        super().__init__()
        self.where_params = where_params

    def append_params(self) -> None:
        if self.where_params:
            self._query += " WHERE " + " AND ".join([
                "{}={}".format(item, f'{value!r}')
                for item, value
                in self.where_params.items()
            ])

    def add_query_end(self) -> None:
        self._query += ";"


class UpdateBaseQuery(ConditionalQuery):

    def __init__(self, data: Dict, **where_params):
        super().__init__(**where_params)
        self.data = data

    def append_params(self) -> None:
        self._query += ",".join([
            "{}={}".format(item, f'{value!r}')
            for item, value
            in self.data.items()
        ])
        super().append_params()


class GetWordQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = """
            SELECT label as label, weight as weight FROM word
        """


class CreateBaseQuery(QueryInterface):

    def __init__(self, data: List[Dict]):
        self.data = data
        self.order = list()

    def append_params(self) -> None:
        self._query += ",".join([
            f"""({','.join([
                    f'{data_item.get(order_item)!r}'
                    for order_item in self.order
            ])})""" for data_item in self.data
        ])

    def add_query_end(self) -> None:
        self._query += ";"


class CreateDocumentQuery(CreateBaseQuery):

    def create_base(self) -> None:
        self.order = ['link']
        self._query = f"""
            INSERT INTO 
            document({', '.join(self.order)})
            VALUES """


class CreateWordQuery(CreateBaseQuery):

    def create_base(self) -> None:
        self.order = ['label', 'weight']
        self._query = f"""INSERT INTO 
            word({', '.join(self.order)}) VALUES"""


class GetDocumentQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = """SELECT link FRON document"""


class GetWordDocumentAssotiationQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = """
            SELECT label as label, weight as weight, link as link
            FROM word join word_document_assotiation
            ON word.id = word_document_assotiation.word_id
            JOIN document ON
            document.id = word_document_assotiation.document_id
        """


class UpdateWordQuery(UpdateBaseQuery):

    def create_base(self) -> None:
        self._query = "UPDATE word SET "


class UpdateDocumentQuery(UpdateBaseQuery):

    def create_base(self) -> None:
        self._query = "UPDATE document SET "


class DeleteWordQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = "DELETE FROM word"


class DeleteDocumentQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = "DELETE FROM document"
