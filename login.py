class Login():

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password


    def setPassword(self, password):
        self.password = password

    def setUser(self, user):
        self.user = user

