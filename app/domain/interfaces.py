from abc import ABC, abstractmethod
from typing import List, Dict, Tuple
from domain.models import Model


class DatabaseConnectionInterface(ABC):

    def __init__(
        self,
        database: str,
        migration: str = None
    ):
        self.database: str = database
        self.migration: str = migration

    @abstractmethod
    def connect(self):
        """Initialize the connection."""

    @abstractmethod
    def close(self):
        """Close the cursor."""

    @abstractmethod
    def commit(self):
        """Save all changes."""

    @abstractmethod
    def get(self) -> List:
        """Returns all values from query."""

    @abstractmethod
    def execute(self, query: str, params: Tuple) -> Dict[str, any]:
        """Execute queries"""

    @abstractmethod
    def migrate(self):
        "Apply migrations for databasse."

class QueryInterface(ABC):

    def __init__(self):
        self._query: str = ""

    def build(self) -> str:
        self.create_base()
        self.append_params()
        self.add_query_end()
        return self._query

    @abstractmethod
    def create_base(self) -> None:
        """Create base structure of query."""

    @abstractmethod
    def append_params(self) -> None:
        """Append additional params in query base."""

    @abstractmethod
    def add_query_end(self) -> None:
        """Added end in query."""


class QueryFactory(ABC):

    @abstractmethod
    def create_query(self, model: type, data: List[Dict]) -> str:
        """Return query for updating special sctructure."""

    @abstractmethod
    def get_query(self, model: type, **where_params) -> str:
        """Return query fot getting sepcial structure."""

    @abstractmethod
    def update_query(self, model: type, data: Dict, **where_params) -> str:
        """Return query for updating special structure."""

    @abstractmethod
    def delete_query(self, model: type, **where_params) -> str:
        """Return query for deleting special structure."""

    @abstractmethod
    def count_query(self, model: type, **where_params) -> str:
        """Return query for counting special structure."""


class DatabaseManagerInterface(ABC):

    def __init__(
        self,
        database_connection: DatabaseConnectionInterface,
        query_creator: QueryFactory
    ):
        self.query_creator = query_creator
        self.database_connection = database_connection

    @abstractmethod
    def get(self, model: type, **where_params) -> List[Model]:
        """Returns models by parameters."""

    @abstractmethod
    def update(self, model: type, data: Dict, **where_params) -> None:
        """Update entities in database."""

    @abstractmethod
    def create(self, model: type, data: List[Model]) -> None:
        """Create models in database."""

    @abstractmethod
    def delete(self, model: type, **where_params) -> None:
        """Delete entities from database."""

    @abstractmethod
    def count(self, model: type, **where_params) -> int:
        """Counts entities in database"""


class ModelMapperInterface(ABC):

    @abstractmethod
    def get(self, **where_params) -> str:
        """Returns get query."""

    @abstractmethod
    def update(self, data: Dict, **where_params) -> str:
        """Returns update query."""

    @abstractmethod
    def create(self, data: List[Dict]) -> str:
        """Returns create query."""

    @abstractmethod
    def delete(self, **where_params) -> str:
        """Returns delete query."""

    def count(self, **where_params) -> str:
        """Counts entities by criteria."""


class ScrapperInterface(ABC):

    def __init__(self, link: str) -> None:
        self.link = link
        self._raw_data: str
        self._prepare_data: str
        self._tokens: List[str]

    def execute(self) -> List[str]:
        self.get_data()
        self.scrape()
        self.tokenize()
        return self._tokens

    @abstractmethod
    def get_data(self):
        """Sends request and
        returns data from page."""

    @abstractmethod
    def scrape(self):
        """Prepares information
        from raw data."""

    @abstractmethod
    def tokenize(self):
        """Create tokens from prepare data."""


class ScraperFactory(ABC):

    def __init__(self):
        self.tokens: List[str]
        self.domain: str
        self.domain_scrapper_mapper: Dict[
            str, ScrapperInterface]

    def get_tokens(self, link: str) -> List[str]:
        self.link = link
        self.analyze_request()
        self.create_tokens()
        return self.tokens

    @abstractmethod
    def analyze_request(self):
        """Alinalization of link and
        mapping with existing scraper."""

    def create_tokens(self):
        self.tokens = self.domain_scrapper_mapper\
            .get(self.domain)(self.link).execute()

class ActionInterface(ABC):

    def __init__(
        self, 
        database_manager: DatabaseManagerInterface
    ):
        self.database_manager = database_manager

    def execute(self):
        """Main method for each action"""
