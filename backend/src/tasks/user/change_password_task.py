from src.core.interfaces.password_tools import PasswordToolsInterface
from src.core.interfaces.logging import LoggingInterface
from src.core.entities.user import User
from ..task_interface import TaskInterface
from src.core.services.employees import Employees


class ChangePasswordTask(TaskInterface[User]):

    def __init__(
            self,
            logging: LoggingInterface,
            password_tools: PasswordToolsInterface,
            employees: Employees) -> None:
        self.logging = logging
        self.password_tools = password_tools
        self.employees = employees

    def run(self, user_change_password):

        if user_change_password['user_kind'] == 'employee':
            employee = self.employees.one_by_username(
                user_change_password['username'])

            if employee is None:
                self.logging.info(
                    'unable to find user with username: ' +
                    user_change_password[
                        'username'])
                return False

            same_password = self.password_tools.validate(
                employee.password,
                user_change_password[
                    'old_password'])

            if not same_password:
                self.logging.info(
                    'password does not match for user with username: ' +
                    user_change_password[
                        'username'])
                return False

            if not self.employees.update_password(
                    user_change_password['username'],
                    self.password_tools.generate_hashed_password(
                        user_change_password['new_password'])):
                return False

        return True
