from flask_bcrypt import Bcrypt


from ..interfaces.password_tools import PasswordToolsInterface


class PasswordTools(PasswordToolsInterface):

    def __init__(self, bcrypt: Bcrypt) -> None:
        self.bcrypt = bcrypt

    def validate(self, hashed_password: str, password: str) -> bool:
        return self.bcrypt.check_password_hash(hashed_password, password)

    def generate_hashed_password(self, password: str) -> str:
        return self.bcrypt.generate_password_hash(password).decode('utf-8')
