from domain.actions import Core
from infrastructure.database.database_connection import DatabaseConnection
from infrastructure.database.query_creator import QueryCreator
from infrastructure.database.database_manager import DatabaseManager
from infrastructure.web_scraping.scraper_creator import ScraperCreator
from view.search_window import SearchWindow


class Programm():

    def __init__(
        self,
        migration: str,
        database: str
    ):
        self.database_connection = DatabaseConnection(
            database=database, migration=migration
        )
        self.query_creator = QueryCreator()
        self.database_manager = DatabaseManager(
            database_connection=self.database_connection,
            query_creator=self.query_creator
        )
        self.scraper_creator = ScraperCreator()
        self.core = Core(
            database_manager=self.database_manager,
            scraper_creator=self.scraper_creator
        )
        self.window = SearchWindow(core=self.core)

    def process(self):
        self.window.apply()
