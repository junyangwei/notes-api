"""连接MySQL公共方法[后面会使用Django对MySQL的ORM映射，暂时不使用这种方式]"""
import MySQLdb

class DBConnect():
    """连接数据库操作"""
    _instance = None

    def init_mysql():
        """返回数据为字典的格式，指定cursorclass"""
        connect = MySQLdb.connect(
            host='127.0.0.1',
            user='notes',
            password='test',
            database='notes',
            port=3306,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
        )
        cur = connect.cursor()
        return cur

    def __init__(self):
        self.cur = DBConnect.init_mysql()

    def get_connect(self):
        return self.connect
