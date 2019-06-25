import pymysql
class MySqlConnect:
    def Mysqlconnect(self,Hostname,dbusername,password,dbname):
        #connect
        db_connection = pymysql.connect(Hostname,dbusername,password,dbname)
        # Making Cursor Object For Query Execution
        cursor = db_connection.cursor()
        return db_connection,cursor
