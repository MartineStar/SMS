import pymysql


def islogin(user_number, pwd, right_id):
    '''该函数用来从数据库中验证登录信息'''
    ADDR = (('127.0.0.1', 10000))
    db = pymysql.connect('localhost', 'root', '123456', 'college', charset='utf8')
    cursor = db.cursor()
    sql = "select * from user where user_number='{}' and password='{}' and type={};".format(user_number, pwd, right_id)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        cursor.close()
        db.close()
        return True
    else:
        cursor.close()
        db.close()
        return


