DEBUG = True
 
DIALECT = 'mysql'
DIRVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '12345678'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'twitter'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DIRVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False