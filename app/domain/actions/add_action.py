from domain.interfaces import ActionInterface
from domain.interfaces import DatabaseManagerInterface


class AddAction(ActionInterface):

    def __init__(
        self,
        database_manager: DatabaseManagerInterface,
        link: str
    ):
        super().__init__(database_manager=database_manager)
        self.link = link

    def execute(self):
        print(self.link)