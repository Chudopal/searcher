import re
import requests
import pymorphy2
from bs4 import BeautifulSoup

from domain.interfaces import ScrapperInterface

class WikiScrapper(ScrapperInterface):

    def get_data(self):
        self._raw_data = requests.get(self.link).text

    def scrape(self):
        fragments  = BeautifulSoup(
                self._raw_data,
                "html.parser"
            ).find(
                    id='bodyContent'
                ).find_all('p')

        self._prepare_data = re.sub(
            "\[[\d, \w]*\]|,|\.|!|:|#|'|\(|\)|\n|\[|\]",
            " ",
            " ".join((
                    fragment.text for fragment in fragments
                ))
            )

    def tokenize(self):
        morph = pymorphy2.MorphAnalyzer()
        words = self._prepare_data.split()
        self._tokens = [
            morph.parse(token)[0].normal_form
            for token in words
        ]
