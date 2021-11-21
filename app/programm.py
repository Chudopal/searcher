from domain.models import Word
from domain.models import Document
from domain.actions import Core
from domain.models import WordDocumentAssotiation
from infrastructure.database.database_connection import DatabaseConnection
from infrastructure.database.query_creator import QueryCreator
from infrastructure.database.database_manager import DatabaseManager
#from infrastructure.web_scraping.wiki_scraper import WikiScrapper
from infrastructure.database.model_database_mapper import WordMapper
from infrastructure.database.model_database_mapper import DocumentMapper
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
        self.model_mapper = {
            Word: WordMapper,
            Document: DocumentMapper,
            WordDocumentAssotiation: "",
        }
        self.query_creator = QueryCreator(
            model_mapper=self.model_mapper
        )
        self.database_connection = DatabaseManager(
            database_connection=self.database_connection,
            query_creator=self.query_creator
        )
        self.core = Core(database_manager=self.database_connection)
        self.window = SearchWindow(core=self.core)

    def process(self):
        self.window.apply()
