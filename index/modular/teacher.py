import pymysql

class Teacher():
    def __init__(self):
        #1.创建数据库连接对象
        self.conn = pymysql.connect('localhost','root','123456','college',charset='utf8')
        #2.创建游标对象
        self.cursor1 = self.conn.cursor()

    # 插入教师个人详细信息
    def add_teacher(self,tea_number,name,gender,data_birth,major_number,phone=None,QQ=None):
        sql ="insert into teacher values('%s','%s','%s','%s','%s','%s','%s');"%(tea_number,name,gender,data_birth,major_number,phone,QQ)
        #查询前一条sql语句执行后受影响行数
        sql1='select row_count();'
        try:
            self.cursor1.execute(sql)
            self.cursor1.execute(sql1)
            self.conn.commit()
            data=self.cursor1.fetchall()
            #判断返回受影响的行数，返回1则表示更新成功，返回OK
            if data[0][0] == 1:
                return 'ok'
            return 'Fail'
        except Exception as e:
            return e

    def update_teacher(self,number,gender=None,data_birth=None,phone=None,QQ=None):
        d1 = {'gender':gender,'data_birth':data_birth,'phone':phone,'QQ':QQ}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            return 'false'
        else:
            sql = "update teacher set "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s',"%d2[n]
            sql = sql[0:-1]
            sql += " where tea_number= '%s';"%number
        try:
            self.cursor1.execute(sql)
            self.conn.commit()
            return 'ok'
        except Exception as e:
            return 'false'


    # 教师通讯录
    def phone_book(self):
        teah_select ="select name,home_address,phone,QQ from teacher;"
        try:
            self.cursor1.execute(teah_select)
            self.conn.commit()
            data=self.cursor1.fetchall()
            if not data:
                return 'none'
            return data#返回元祖，元组内为一个个元祖
        except Exception as e:
            return 'false'

    # 录入学生成绩
    def insert_sscore(self,term,major_number,class_number,stu_number,course_number,score):
        sql="insert into score(term,major_number,class_number,stu_number,course_number,score) value('%s',%d,%d,%d,%d,%d);"%(term,major_number,class_number,stu_number,course_number,score)

        try:
            self.cursor1.execute(sql)
            self.conn.commit()
            data=self.cursor1.fetchall()
            if not data:
                return 'FIAL'
            return 'ok'#返回元祖，元组内为一个个元祖
        except Exception as e:
            return 'false'

    # 选择班级返回总分成绩和班级排名
    def score_paiming(self,class_number):
        sql ='select score.stu_number,student.name,sum(score.score) as zongfen,score.class_number from score left join student on score.stu_number=student.stu_number where score.class_number=%d group by score.stu_number,student.name order by sum(score.score) desc;'% class_number
        try:
            self.cursor1.execute(sql)
            self.conn.commit()
            data=self.cursor1.fetchall()
            print(data)
            if not data:
               return 'none'
            return data#返回元祖，元组内为一个个元祖
        except Exception as e:
            return 'false'

    #输入用户user_number,新密码newpassword,执行修改用户密码操作
    def update_pwd(self,user_number,newpassword):
        sql='update user set password=%d where user_number=%d;'%(newpassword,user_number)
        #查询前一条sql语句执行后受影响行数
        sql1='select row_count();'
        try:
            self.cursor1.execute(sql)
            self.cursor1.execute(sql1)
            self.conn.commit()
            data=self.cursor1.fetchall()
            #判断返回受影响的行数，返回1则表示更新成功，返回OK
            if data[0][0] == 1:
               return 'ok'
            return 'Fail'
        except Exception as e:
            return 'false'

    def close(self):
        self.cursor1.close()
        self.conn.close()

teacher=Teacher()
# teacher.inst_teacher(7,'小飞',1,19980999,'汉',8,'广州天河',15777778,46110979)
# print(teacher.phone_book())
# b=teacher.insert_sscore('第一学期',111,333,1,105,100)
# print(teacher.score_paiming(333))
#print(teacher.update_pwd(2,8233333))
teacher.close()
