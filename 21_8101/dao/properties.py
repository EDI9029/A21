class common_db:
    def __init__(self, host, port, user, password, db, charset):
        self._host = host
        self._port = port 
        self._user = user 
        self._password = password
        self._db = db
        self._charset = charset 
    
    def get_host(self):
        return self._host

    def get_port(self):
        return self._port

    def get_user(self):
        return self._user
    
    def get_password(self):
        return self._password

    def get_db(self):
        return self._db
    
    def get_charset(self):
        return self._charset
    
    def set_host(self, new_host):
        self._host = new_host 

    def set_port(self, new_port):
        self._port = new_port
    
    def set_user(self, new_user):
        self._user = new_user 
    
    def set_password(self, new_password):
        self._password = new_password
    
    def set_db(self, new_db):
        self._db = new_db

    def set_charset(self, new_charset):
        self._charset = new_charset 

kd_21 = common_db('localhost', 3306, 'root', 'usaac130h41y799q', 'kd21', 'utf8')