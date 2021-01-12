from src.core.interfaces.logging import LoggingInterface
from src.core.entities.user import User
from ..task_interface import TaskInterface
from src.core.services.employees import Employees


class RefreshTask(TaskInterface[User]):

    def __init__(
            self,
            logging: LoggingInterface,
            employees: Employees) -> None:
        self.logging = logging
        self.employees = employees

    def run(self, user):

        if user['user_kind'] == 'employee':

            emp_roles = self.employees.roles(user['username'])

            if len(user['roles']) == 0 or len(emp_roles) == 0:
                return False

            user_roles = set(user['roles'])
            employee_roles = set(emp_roles)

            role_diff_count = len(user_roles.difference(employee_roles)) + len(
                employee_roles.difference(user_roles))

            if role_diff_count > 0:
                return False

            return True

        return False
