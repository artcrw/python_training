import pymysql.cursors


class DbFixture:
    def __init__(self, host, name, user, password, port):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.port = port
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, port=port)

    def destroy(self):
        self.connection.close()