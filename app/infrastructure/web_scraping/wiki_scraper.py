import re
from bs4 import BeautifulSoup

from infrastructure.web_scraping.web_scraper import WebScraper


class WikiScrapper(WebScraper):

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

