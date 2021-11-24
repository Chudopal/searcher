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
        self.create_condition()

    def create_condition(self):
        super().append_params()


class GetWordQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = """
            SELECT id as id, label as label, weight as weight FROM word
        """


class CreateBaseQuery(QueryInterface):

    def __init__(self, data: List[Dict]):
        self.data = data
        self.order: List[str] = list()
        self.conflict_fields: List[str] = list()

    def append_params(self) -> None:
        self._query += ",".join([
            f"""({','.join([
                    f'{data_item.get(order_item)!r}'
                    for order_item in self.order
            ])})""" for data_item in self.data
        ])

    def add_query_end(self) -> None:
        self._query += f"""
            ON CONFLICT({", ".join(
                [str(field) for field
                in self.conflict_fields]
            )}) DO
        """
        self.initialize_update()
        self._query += " ;"

    def initialize_update(self):
        self._query += """ UPDATE SET """
        self._query += " ,".join([
            "{}=excluded.{}".format(key, key)
            for key in self.data[0].keys()
        ])


class CreateDocumentQuery(CreateBaseQuery):

    def create_base(self) -> None:
        self.conflict_fields = ['link']
        self.order = ['link']
        self._query = f"""
            INSERT INTO 
            document({', '.join(self.order)})
            VALUES """


class CreateWordQuery(CreateBaseQuery):

    def create_base(self) -> None:
        self.conflict_fields = ['label']
        self.order = ['label', 'weight']
        self._query = f"""INSERT INTO 
            word({', '.join(self.order)}) VALUES """


class CreateWordDocumentAssotiationQuery(CreateBaseQuery):

    def create_base(self) -> None:
        self.conflict_fields = ['word_id']
        self._query = """
            INSERT INTO
            word_document_assotiation(word_id, document_id, coefficient)
            VALUES
        """

    def append_params(self) -> None:
        self._query += ", ".join([
            """((SELECT id FROM word WHERE label={}),
                (SELECT id FROM document WHERE link={}),
                {}
            )""".format(
                    f"{item.get('label')!r}",
                    f"{item.get('link')!r}",
                    item.get('coefficient')
                ) for item in self.data
        ])

    def initialize_update(self):
        self._query += """ UPDATE SET """
        self._query += "coefficient=excluded.coefficient"

class GetDocumentQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = """SELECT id as id, link as link FRON document"""


class GetWordDocumentAssotiationQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = """
            SELECT label as label, weight as weight, link as link,
            coefficient as coefficient
            FROM word join word_document_assotiation
            ON word.id = word_document_assotiation.word_id
            JOIN document ON
            document.id = word_document_assotiation.document_id
        """


class UpdateWordQuery(UpdateBaseQuery):

    def create_base(self) -> None:
        self._query = "UPDATE word SET "

    def create_condition(self):
        if self.where_params:
            self._query += " WHERE " + " AND ".join([
                "word_id IN (SELECT id FROM word WHERE label = {})".format(
                    f'{self.where_params.get("label")!r}'
                ),
                "document_id IN (SELECT id FROM document WHERE link = {})".format(
                    f'{self.where_params.get("link")!r}'
                ),
            ])


class UpdateDocumentQuery(UpdateBaseQuery):

    def create_base(self) -> None:
        self._query = "UPDATE document SET "


class UpdateWordDocumentAssotiationQuery(UpdateBaseQuery):

    def create_base(self) -> None:
        self._query = "UPDATE word_document_assotiation "


class DeleteWordQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = "DELETE FROM word "


class DeleteDocumentQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = "DELETE FROM document "


class DeleteWordDocumentAssotiationQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = "DELETE FROM word_document_assotiation "

class CountWordDocumentAssotiationQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = """
            SELECT count(*) from word_document_assotiation
            JOIN word ON word_id=word.id
            JOIN document ON document_id = document.id
        """


class CountWordQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = "SELECT count(*) from word "


class CountDocumentQuery(ConditionalQuery):

    def create_base(self) -> None:
        self._query = "SELECT count(*) from document "