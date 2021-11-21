from math import log
from typing import List

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
        self.inverse_frequency: float
        self.documents_number: int
        self.documents_number_with_word: int

    def execute(self):
        self.get_tokens()
        self.get_data()
        self.calculate_inverse_frequency()
        self.calculate_word_weight()

    def get_tokens(self):
        self.tokens = self.scraper_creator\
            .get_tokens(self.link)

    def save_new_data(self):
        pass

    def get_documents_number(self):
        self.documents_number = self.database_manager.count(Document)

    def get_documents_number_with_word(self, word_label):
        self.documents_number_with_word =\
            self.database_manager.count(
                WordDocumentAssotiation, label=word_label
            )

    def calculate_inverse_frequency(self):
        self.inverse_frequency = log(
            (self.documents_number/
                self.documents_number_with_word),
            10
        )

    def calculate_word_weight(self):
        pass