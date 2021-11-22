from math import sqrt
import numpy as np
import pymorphy2
from typing import List
from numpy import linalg as LA
from domain.models import WordDocumentAssotiation

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
        self.word_assotiations: List[str] = list()
        self.word_vector: List[float] = list()
        self.document_vector: List[List] = list()
        self.result: List[str] = list()
        self.words: List[str] = list()
        self.documents: List[str] = list()

    def execute(self):
        self.prepare_request()
        self.create_word_vector()
        self.create_document_vector()
        self.aggregate_similarity()
        self.sort_result()
        return self.result

    def prepare_request(self):
        morph = pymorphy2.MorphAnalyzer()
        self.request = self.request.lower()
        words = self.request.split()
        self.words = [
            morph.parse(token)[0].normal_form
            for token in words
        ]
        [
            self.word_assotiations.extend(
                self.get_word_document_assotiation(word)
            ) for word in words
        ]

    def get_word_document_assotiation(self, word_label):
        return self.database_manager.get(
            WordDocumentAssotiation,
            label=word_label
        )

    def create_word_vector(self):
        sum_sqrt = self.find_sum_sqrt()
        self.word_vector = [
            word_assotiation.coefficient/sum_sqrt
            for word_assotiation
            in self.word_assotiations]

    def create_document_vector(self):
        self.word_document_mapper = {
            doc_assotiation.document.link: [
                (lambda: 1 if (word_assotiation.document.link ==
                    doc_assotiation.document.link) else 0)()
                for word_assotiation
                in self.word_assotiations
            ]
            for doc_assotiation in self.word_assotiations
        }

    def find_sum_sqrt(self) -> float:
        return sqrt(sum((
                word_assotiation.coefficient**2
                for word_assotiation
                in self.word_assotiations
        )))

    def aggregate_similarity(self):
        for document, document_vector in self.word_document_mapper.items():
            self.word_document_mapper[document] =\
                self.calculate_similarity(
                    document_vector=document_vector
                )

    def sort_result(self):
        [ self.result.extend([
                link for link, not_sort_weight
                in self.word_document_mapper.items()
                if not_sort_weight == weight
            ]) for weight in sorted(
                self.word_document_mapper.values()
            )
        ]

    def calculate_similarity(self, document_vector):
        np_word_vector = np.array(self.word_vector)
        np_document_vector = np.array(document_vector)
        word_vector_normal = LA.norm(np_word_vector)
        document_vector_normal = LA.norm(np_document_vector)
        semularity = (np.dot(np_word_vector, np_document_vector)/
            (word_vector_normal * document_vector_normal))
        return float(semularity)