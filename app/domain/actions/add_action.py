from math import log
from typing import Dict, List

from domain.models import Word
from domain.models import Document
from domain.models import WordDocumentAssotiation

from domain.interfaces import ActionInterface
from domain.interfaces import DatabaseManagerInterface
from domain.interfaces import ScraperFactory


class AddAction(ActionInterface):

    def __init__(
        self,
        database_manager: DatabaseManagerInterface,
        scraper_creator: ScraperFactory,
        link: str
    ):
        super().__init__(
            database_manager=database_manager
        )
        self.scraper_creator = scraper_creator
        self.link = link
        self.tokens: List[str]
        self.words: List[Dict] = list()
        self.inverse_frequency: float
        self.documents_number: int
        self.documents_number_with_word: int

    def execute(self):
        self.save_document()
        self.get_tokens()
        self.process_tokens()

    def save_document(self):
        self.database_manager.create(
            Document, [{'link': self.link}]
        )

    def get_tokens(self):
        self.tokens = self.scraper_creator\
            .get_tokens(self.link)

    def process_tokens(self):
        self.get_documents_number()
        for token in self.tokens:
            documents_number_with_word =\
                self.get_documents_number_with_token(token)
            weight = self.calculate_weight(
                documents_number_with_word=documents_number_with_word
            )
            self.words.append(
                {'label': token, 'weight': weight}
            )
            word_documant_frequency =\
                self.calculate_word_documant_frequency(token)
            coefficient = self.calculate_coefficient(
                frequency=word_documant_frequency,
                weight=weight
            )
        self.save_data()

    def save_data(self):
        self.database_manager.create(
            Word,
            self.words
        )

    def get_documents_number(self):
        self.documents_number =\
            self.database_manager.count(Document)

    def get_documents_number_with_token(
        self, word_label
    ) -> int:
        number = self.database_manager.count(
            WordDocumentAssotiation,
            label=word_label
        )
        return number if number else 1

    def calculate_weight(
        self, documents_number_with_word: int
    ) -> float:
        return log(
            self.documents_number/documents_number_with_word,
            10
        )

    def calculate_word_documant_frequency(self, word) -> int:
        return self.tokens.count(word)

    def calculate_coefficient(
        self, frequency: int, weight: float
    ) -> float:
        return frequency * weight

    def calculate_word_weight(self):
        pass