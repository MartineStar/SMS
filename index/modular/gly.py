#!/usr/bin/env python3
#coding=utf-8

'''
name = xhl
功能：提供管理员模块功能实现的接口
'''
import pymysql
import time as T


class Administrators():
    def __init__(self):
        self.db = pymysql.connect('localhost','root','123456','college',charset='utf8')
        self.cur = self.db.cursor()

    #管理员添加全员信息(user表),同时判断用户类型，插入对应表格当中
    def add_user(self,number,name,mytype):
        try:
            sql1 = "insert into user(user_number,name,type) values('%s','%s',%s);"%(number,name,mytype)
            self.cur.execute(sql1)
            self.db.commit()
            # if mytype == '0':
            #     major_name = number[:-4]
            #     major_number = self.cur.execute("select * from major where major_name='%s'"%(major_name))[0][0]
            #     class_number = number[:-2]
            #     sql2 = "insert into student(stu_number,name,gender,major_number,class_number,) values('%s','%s',0,'%s','%s');"%(number,name,major_number,class_number)
            #     self.cur.execute(sql2)
            #     self.db.commit()
            # elif mytype == '1':
            #     sql3 = "insert into teacher(tea_number,name) values('%s','%s');"%(number,name)
            #     self.cur.execute(sql3)
            #     self.db.commit()
            return 'ok'
        except Exception as e:
            return e

    #管理员删除某位信息(通过用户编号及名字删除)(user表)
    def del_user(self,number,name=None):
        try:
            sql = "delete from user where user_number = '%s';"%(number)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'

    #修改信息(user表)
    def update_user(self,number,new_pwd):
        try:
            sql = "update user set password = '%s' where user_number = '%s';"%(new_pwd,number)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return e

    #修改学生和教师权限(user表)
    def update_isActive(self,type,isActive):
        try:
            sql = "update user set isActive = '%s' where type = '%s';"%(isActive,type)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return e

    #管理员查看user表(全员表)
    def check_user(self,number=None,name=None,password=None,mytype=None,isActive=None):
        d1 = {'user_number':number,'name':name,'password':password,'type':mytype,'isActive':isActive}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "select * from user;"
        else:
            sql = "select * from user where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data#返回元祖，元组内为一个个元祖
        except Exception as e:
            return 'false' 

    #管理员添加专业名称(major表)
    def add_major(self,number,name):
        try:
            sql = "insert into major values('%s','%s');"%(number,name)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return e

    #管理员删除专业(major表)
    def del_major(self,number=None,name=None):
        d1 = {'major_number':number,'major_name':name}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "delete from major;"
        else:
            sql = "delete from major where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'

    #管理员修改专业(major表)
    def update_major(self,number,new_number,new_name):
        try:
            sql = "update major set major_number = '%s', major_name = '%s' where major_number = '%s';"%(new_number,new_name,number)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'
    
    #管理员查看专业表(major表)
    def check_major(self,number=None,name=None):
        d1 = {'major_number':number,'major_name':name}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "select * from major;"
        else:
            sql = "select * from major where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data
        except Exception as e:
            return 'false' 

    # 管理员添加班级(clazz表)
    def add_clazz(self,number,name,clazz_major):
        try:
            sql = "insert into clazz values('%s','%s','%s');"%(number,name,clazz_major)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'

    #管理员删除班级(clazz表)
    def del_clazz(self,number=None,name=None,clazz_major=None):
        d1 = {'clazz_number':number,'clazz_name':name,'clazz_major':clazz_major}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "delete from clazz;"
        else:
            sql = "delete from clazz where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'

    #管理员查看班级(clazz表)
    def check_clazz(self,number=None,name=None,clazz_major=None):
        d1 = {'clazz_number':number,'clazz_name':name,'clazz_major':clazz_major}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "select * from clazz;"
        else:
            sql = "select * from clazz where "
            for n in d2:
                sql += '%s'%n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data
        except Exception as e:
            return 'false' 



    #管理员添加专业课程安排(major_course表)
    def add_m_c(self,maj_numb,cou_numb,cla_numb,tea_numb,place,day,time,week,date):
        #day格式：2018/1/1
        x,y,z=day.split('/')
        asc = T.mktime((int(x),int(y),int(z),0,0,0,0,0,0))
        # week = T.localtime(asc)[6] 
        try:
            sql = "insert into major_course values\
            (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(maj_numb,cou_numb,cla_numb,tea_numb,place,day,time,week,date)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return e

    #管理员删除专业课程安排(major_course表)
    def del_m_c(self,id=None,maj_numb=None,cou_numb=None,cla_numb=None,tea_numb=None,place=None,day=None,time=None,date=None):
        d1 = {'id':id,'major_number':maj_numb,'course_number':cou_numb,'class_number':cla_numb,'tea_number':tea_numb,'course_place':place,'course_day':day,'course_time':time,'course_date':date}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "delete from major_course"
        else:
            sql = "delete from major_course where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'

    #管理员修改专业课程安排(major_course表)
    def update_m_c(self,m_numb,c_numb,t_numb,day,time,new_c_numb=None,new_t_numb=None,new_place=None,new_day=None,new_time=None,new_date=None):
        d1 = {'class_number':new_c_numb,'tea_number':new_t_numb,'course_place':new_place,'course_day':new_day,'course_time':new_time,'course_date':new_date}
        if new_day != None:
            x,y,z=day.split('-')
            asc = T.mktime((int(x),int(y),int(z),0,0,0,0,0,0))
            week = T.localtime(asc)[6] 
            d1['course_week']=week
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            return 'false'
        else:
            sql = "update major_course set "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s',"%d2[n]
            sql = sql[0:-1]
            sql += " where major_number='%s' and course_number='%s'and tea_number='%s' and course_day='%s' and course_time='%s';"%(m_numb,c_numb,t_numb,day,time)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'
    
    #管理员查看专业课程安排(major_course表)
    def check_m_c(self,ID=None,maj_numb=None,cou_numb=None,cla_numb=None,tea_numb=None,place=None,day=None,time=None,week=None,date=None):
        d1 = {'ID':ID,'major_number':maj_numb,'course_number':cou_numb,'class_number':cla_numb,'tea_number':tea_numb,'course_place':place,'course_day':day,'course_time':time,'course_week':week,'course_date':date}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "select * from major_course;"
        else:
            sql = "select * from major_course where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data
        except Exception as e:
            return 'false'

    #管理员添加考试安排(exam表)
    def add_exam(self,term,maj_numb,class_number,course_name,e_place,e_day,e_time):
        try:
            sql = "insert into exam values\
            (null,'%s','%s','%s','%s','%s','%s','%s');"%(term,maj_numb,class_number,course_name,e_place,e_day,e_time)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return e

    #管理员删除考试安排(exam表)
    def del_exam(self,ID=None,term=None,maj_numb=None,class_number=None,course_name=None,e_place=None,e_day=None,e_time=None,):
        d1 = {'ID':ID,'term':term,'major_number':maj_numb,'class_number':class_number,'course_name':course_name,'exam_place':e_place,'exam_day':e_day,'exam_time':e_time}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "delete from exam"
        else:
            sql = "delete from exam where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'

    #管理员修改考试安排(exam表)
    def update_exam(self,ID,new_e_place=None,new_e_day=None,new_e_time=None):
        d1 = {'exam_place':new_e_place,'exam_day':new_e_day,'exam_time':new_e_time}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            return 'false'
        else:
            sql = "update exam set "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s',"%d2[n]
            sql = sql[0:-1]
            sql += " where ID= '%s';"%ID
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'
    
    #管理员查看考试安排(exam表)
    def check_exam(self,ID=None,term=None,maj_numb=None,class_number=None,course_name=None,e_place=None,e_day=None,e_time=None):
        d1 = {'ID':ID,'term':term,'major_number':maj_numb,'class_number':class_number,'course_name':course_name,'exam_place':e_place,'exam_day':e_day,'exam_time':e_time}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "select * from exam;"
        else:
            sql = "select * from exam where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data
        except Exception as e:
            return 'false' 

    #管理员添加成绩(score表)
    def add_score(self,term,major_number,cla_numb,stu_numb,cou_numb,score,maj_name):
        try:
            sql = "insert into score values(null,'%s','%s','%s','%s','%s','%s','%s');"%(term,major_number,cla_numb,stu_numb,cou_numb,score,maj_name)
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return sql

    #管理员删除成绩(score表)
    def del_score(self,cla_numb=None,stu_numb=None,cou_numb=None,maj_name=None):
        d1 = {'class_number':cla_numb,'stu_number':stu_numb,'course_number':cou_numb,'major_name':maj_name}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "delete from score"
        else:
            sql = "delete from score where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'

    #管理员修改成绩(score表)
    def update_score(self,cla_numb,stu_numb,course_number,new_score):
        sql = "update score set score='%s' where class_number='%s' and stu_number='%s' and course_number='%s';"%(new_score,cla_numb,stu_numb,course_number)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'
    
    #管理员查看成绩(score表)
    def check_score(self,id=None,cla_numb=None,stu_numb=None,cou_numb=None,major_name=None):
        d1 = {'ID':id,'class_number':cla_numb,'stu_number':stu_numb,'course_number':cou_numb,'major_name':major_name}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "select * from score;"
        else:
            sql = "select * from score where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data
        except Exception as e:
            return 'false' 


    #管理员查看student表
    def check_student(self,number=None,name=None,gender=None,major_number=None,class_number=None,instructor=None):
        d1 = {'stu_number':number,'name':name,'gender':gender,'major_number':major_number,'class_number':class_number,'instructor':instructor}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "select * from student;"
        else:
            sql = "select * from student where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data#返回元祖，元组内为一个个元祖
        except Exception as e:
            return sql

    #管理员删除班级的同时将班级里面所有学生信息删除(student表)
    def del_student(self,clazz_name=None,major_number=None):
        if clazz_name == None:
            try:
                sql = "delete from student where major_number = '%s';"%(major_number)
                self.cur.execute(sql)
                self.db.commit()
                return 'ok'
            except Exception as e:
                return 'false'
        elif major_number == None:
            try:
                sql = "delete from student where class_number = '%s';"%(clazz_name)
                self.cur.execute(sql)
                self.db.commit()
                return 'ok'
            except Exception as e:
                return 'false'


    #管理员查看teacher表
    def check_teacher(self,number=None,name=None,gender=None,data_birth=None,major_number=None):
        d1 = {'tea_number':number,'name':name,'gender':gender,'data_birth':data_birth,'major_number':major_number}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            sql = "select * from teacher;"
        else:
            sql = "select * from teacher where "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s' and "%d2[n]
            sql=sql[0:-5]+';'
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data#返回元祖，元组内为一个个元祖
        except Exception as e:
            return 'false' 

    # 管理员查看公告
    def check_notice(self,schoolname=None,teacherBulletin=None,studentBulletin=None):
        sql = "select * from notice;"
        try:
            self.cur.execute(sql)
            self.db.commit()
            data=self.cur.fetchall()
            if not data:
                return 'none'
            return data#返回元祖，元组内为一个个元祖
        except Exception as e:
            return 'false'

    # 管理员修改公告
    def update_notice(self,schoolname=None,teacherBulletin=None,studentBulletin=None):
        if schoolname != None:
            sql = "update notice set schoolname='%s';"%(schoolname)
        elif teacherBulletin != None:
            sql = "update notice set teacherBulletin='%s';"%(teacherBulletin)
        elif studentBulletin != None:
            sql = "update notice set studentBulletin='%s';"%(studentBulletin)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return e

    def close(self):
        self.cur.close()
        self.db.close()


