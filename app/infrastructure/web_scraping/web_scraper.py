import requests
import pymorphy2

from domain.interfaces import ScrapperInterface


class WebScraper(ScrapperInterface):

    def get_data(self):
        self._raw_data = requests.get(self.link).text

    def tokenize(self):
        morph = pymorphy2.MorphAnalyzer()
        words = self._prepare_data.split()
        self._tokens = [
            morph.parse(token)[0].normal_form
            for token in words
        ]
