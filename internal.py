import role, banckaccount

class Internal():
    role: role.Role
    __account: banckaccount.Bankaccount
    def __init__(self, role, __account) -> None:
        self.role=role.Role
        self.__account = banckaccount.Bankaccount

    def biometricvalidat():
        pass