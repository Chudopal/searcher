from domain.interfaces import ActionInterface, ScrapperInterface
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

    def execute(self):
        print(self.scraper_creator.get_tokens(self.link))