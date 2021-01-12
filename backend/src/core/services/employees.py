from typing import List

from src.core.interfaces.logging import LoggingInterface
from src.core.interfaces.data_session import DataSessionInterface
from src.core.entities.employee import Employee
from src.core.services.entities import Entities


class Employees(Entities):

    def __init__(self, logging: LoggingInterface,
                 data_session: DataSessionInterface):
        super().__init__(logging, data_session, Employee, 'employee_id')

    def one_by_username(self, username: str) -> Employee:
        session = self.Session()

        employee = session.query(Employee).filter(
            Employee.username == username).one_or_none()

        session.close()

        return employee

    def roles(self, username: str) -> List[str]:
        session = self.Session()

        sql = """select r.role_name
        from employees as emp
            inner join user_roles as ur
                on emp.username = ur.username and ur.user_kind ='employee'
            inner join roles as r on ur.role_id = r.role_id
        where emp.username = :username;"""

        result = session.execute(sql, {"username": username})

        roles = [r[0] for r in result]

        session.close()

        return roles

    def has_one_or_more_roles(self, username: str, roles: List[str]) -> bool:
        return len([r for r in self.roles(username) if r in roles]) > 0

    def update_password(self, username: str, hashed_password: str) -> None:
        session = self.Session()
        session.query(Employee).filter(Employee.username == username).update({
            "password": hashed_password
        })
        session.commit()
        session.close()

        return True
