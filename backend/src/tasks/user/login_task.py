from src.core.interfaces.password_tools import PasswordToolsInterface
from src.core.interfaces.logging import LoggingInterface
from src.core.entities.user import User
from ..task_interface import TaskInterface
from src.core.services.employees import Employees


class LoginTask(TaskInterface[User]):

    def __init__(
            self,
            logging: LoggingInterface,
            password_tools: PasswordToolsInterface,
            employees: Employees) -> None:
        self.logging = logging
        self.password_tools = password_tools
        self.employees = employees

    def run(self, login_user):

        if login_user['kind'] == 'employee':
            employee = self.employees.one_by_username(login_user['username'])

            if employee is None:
                self.logging.info(
                    'unable to find user with username: ' + login_user[
                        'username'])
                return None

            same_password = self.password_tools.validate(
                employee.password,
                login_user[
                    'password'])

            if not same_password:
                self.logging.info(
                    'password does not match for user with username: ' +
                    login_user[
                        'username'])
                return None

            self.logging.info(
                'user found with username: ' + login_user['username'])

            return User(employee.employee_id,
                        'employee',
                        employee.username,
                        employee.display_name(),
                        self.employees.roles(employee.username))

        return None
