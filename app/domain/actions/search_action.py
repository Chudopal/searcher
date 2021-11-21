import pymorphy2
from typing import List

from domain.interfaces import ActionInterface
from domain.interfaces import DatabaseManagerInterface


class SearchAction(ActionInterface):

    def __init__(
        self,
        database_manager: DatabaseManagerInterface,
        request: str
    ):
        super().__init__(
            database_manager=database_manager
        )
        self.request = request
        self.words: List[str]
        self.word_vector: List[float]

    def execute(self):
        self.prepare_request()
        self.create_vectors()
        self.calculate_similarity()
        return self.documents = [
            "rfrfwrf",
            "wferferfer"
        ]

    def prepare_request(self):
        morph = pymorphy2.MorphAnalyzer()
        words = self._prepare_data.split()
        self.words = [
            morph.parse(token)[0].normal_form
            for token in words
        ]
        print(self.words)

    def create_vactors(self):
        pass