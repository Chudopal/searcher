from urllib.parse import urlparse
from domain.interfaces import ScraperFactory
from infrastructure.web_scraping.wiki_scraper import WikiScrapper


class ScraperCreator(ScraperFactory):

    def __init__(self):
        super().__init__()
        self.domain_scrapper_mapper = {
            "ru.wikipedia.org": WikiScrapper
        }

    def analyze_request(self):
        self.domain = urlparse(self.link).netloc
