import base64


class User:
    user_id = -1
    user_kind = None
    username = None
    display_name = None
    is_authenticated = False
    is_active = False
    is_anonymous = True
    roles = []

    def __init__(self, user_id=-1, user_kind=None, username=None,
                 display_name=None, roles=()):
        self.user_id = user_id
        self.user_kind = user_kind
        self.username = username
        self.display_name = display_name
        self.roles = roles

    def get_id(self):
        compound_id = self.user_kind + ':' + str(self.user_id)
        return base64.b64encode(compound_id.encode('utf-8'))
