#!/usr/bin/env python3
#coding=utf-8

'''
name = xhl
功能：提供管理员模块功能实现的接口
'''
import pymysql
import time as T


class Studentistrators():
    def __init__(self):
        self.db = pymysql.connect('localhost','root','123456','college',charset='utf8')
        self.cur = self.db.cursor()

    # 添加学生信息student表
    def add_student(self,number,name,gender,instructor=None,phone=None,QQ=None):
        maj = number[0:-4]
        sql1 = "select * from major where major_name='%s';"%maj
        self.cur.execute(sql1)
        self.db.commit()
        maj_numb = self.cur.fetchone()[0]
        cla_numb = number[:-2]
        d1 = [number,name,gender,maj_numb,cla_numb,instructor,phone,QQ]
        d2=[]
        for m in d1:
            if m != None:
                d2.append(m)
        sql2 = "insert into student values("
        for n in d2:
            sql2 += "'%s'"%n+','
        sql2=sql2[0:-1]+');'
        # print(sql2)
        try:
            self.cur.execute(sql2)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return sql2
    # 修改学生信息student表
    def update_student(self,number,gender=None,phone=None,QQ=None):
        d1 = {'gender':gender,'phone':phone,'QQ':QQ}
        d2={}
        for m in d1:
            if d1[m] != None:
                d2[m]=d1[m]
        if d2 == {}:
            return 'false'
        else:
            sql = "update student set "
            for n in d2:
                sql += n
                sql += '='
                sql += "'%s',"%d2[n]
            sql = sql[0:-1]
            sql += " where stu_number= '%s';"%number
        try:
            self.cur.execute(sql)
            self.db.commit()
            return 'ok'
        except Exception as e:
            return 'false'
    
    def close(self):
        self.cur.close()
        self.db.close()




