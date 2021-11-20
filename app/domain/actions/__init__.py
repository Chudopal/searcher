from domain.interfaces import DatabaseManagerInterface
from domain.actions.add_action import AddAction
from domain.actions.search_action import SearchAction


class Core():

    def __init__(self, database_manager: DatabaseManagerInterface):
        self.database_manager = database_manager

    def add_action(self, link: str):
        return AddAction(
            database_manager=self.database_manager,
            link=link).execute()

    def search_action(self, request: str):
        return SearchAction(
            database_manager=self.database_manager,
            request=request
        ).execute()