from typing import List

from src.core.interfaces.logging import LoggingInterface
from src.core.entities.user import User
from ..task_interface import TaskInterface
from src.core.services.employees import Employees


class HasOneOrMoreRolesTask(TaskInterface[User]):

    def __init__(
            self,
            logging: LoggingInterface,
            employees: Employees) -> None:
        self.logging = logging
        self.employees = employees

    def run(self, username: str, roles: List[str]):

        return self.employees.has_one_or_more_roles(username, roles)
