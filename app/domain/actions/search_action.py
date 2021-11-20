from domain.interfaces import ActionInterface
from domain.interfaces import DatabaseManagerInterface


class SearchAction(ActionInterface):

    def __init__(
        self,
        database_manager: DatabaseManagerInterface,
        request: str
    ):
        super().__init__(database_manager=database_manager)
        self.request = request

    def execute(self):
        print(self.request)