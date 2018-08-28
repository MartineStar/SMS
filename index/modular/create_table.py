#!/usr/bin/env python3
#coding=utf-8

'''
name = xhl
功能：初始化mysql数据表
'''

import pymysql

class College():
    def __init__(self):
        self.create_db()#自动创建名为college的数据库
        self.db = pymysql.connect('localhost','root','123456','college',charset='utf8')
        self.cur = self.db.cursor()
        self.create_table()#自动创建项目所有数据表
        
    #创建colleage数据库
    def create_db(self):
        db = pymysql.connect('localhost','root','123456',charset='utf8')
        cur = db.cursor()
        try:
            sql = "create database college charset=utf8;"
            cur.execute(sql)
            db.commit()
        except Exception as e:
            pass

    #创建数据表
    def create_table(self):
        try:
            #创建user表
            sql1 = "create table user(\
                    user_number varchar(10) primary key,\
                    name varchar(20) not null,\
                    password varchar(20) not null default '000000',\
                    type char(1) not null,index(name)\
                    isActive varchar(1) not null default '1',\
                    )charset=utf8;"
            #创建student表
            sql2 = "create table student(\
                    stu_number varchar(10),\
                    name varchar(20),\
                    gender char(1) not null,\
                    major_number varchar(3) not null,\
                    class_number varchar(20) not null,\
                    instructor varchar(10) ,\
                    phone varchar(20),\
                    QQ varchar(20),\
                    index(major_number),\
                    index(class_number),\
                    index(instructor),\
                    foreign key(stu_number) references \
                    user(user_number) on delete cascade on update cascade,\
                    foreign key(name) references \
                    user(name) on delete cascade on update cascade\
                    )charset=utf8;"
            
            #创建teacher表
            sql3 = "create table teacher(\
                    tea_number varchar(10),\
                    name varchar(20),\
                    gender char(1) not null,\
                    data_birth varchar(20) not null,\
                    nation varchar(20) not null,\
                    major_number varchar(3) not null,\
                    phone varchar(20),\
                    QQ varchar(20),\
                    index(major_number),\
                    foreign key(tea_number) references \
                    user(user_number) on delete cascade on update cascade,\
                    foreign key(name) references \
                    user(name) on delete cascade on update cascade\
                    )charset=utf8;"
            
            #创建专业名称表
            sql4 = "create table major(\
                    major_number varchar(3) primary key,\
                    major_name varchar(50) not null)charset=utf8;"

            #创建专业课设表
            sql5 = "create table major_course(\
                    ID tinyint primary key auto_increment,\
                    major_number varchar(20) not null,\
                    course_number varchar(50) not null,\
                    class_number varchar(20) not null,\
                    tea_number varchar(10),\
                    course_place varchar(20) not null,\
                    course_day varchar(20) not null,\
                    course_time varchar(50) not null,\
                    course_week varchar(10) not null,\
                    course_date varchar(50) not null,\
                    index(major_number),\
                    index(class_number))charset=utf8;"
            #创建考试安排表
            sql6 = "create table exam(\
                    ID tinyint primary key auto_increment,\
                    term varchar(20) not null,\
                    major_number varchar(50) not null,\
                    class_number varchar(50) not null,\
                    course_name varchar(30) not null,\
                    exam_place varchar(20) not null,\
                    exam_day varchar(20) not null,\
                    exam_time varchar(50) not null,\
                    index(class_name),index(major_number),index(course_name))charset=utf8;"
            #创建成绩查询表
            sql7 = "create table score(\
                    ID tinyint primary key auto_increment,\
                    class_number varchar(20) not null,\
                    stu_number varchar(10) not null,\
                    course_number varchar(3) not null,\
                    score tinyint not null,\
                    major_name varchar(50) not null,\
                    index(class_number),\
                    unique(stu_number))charset=utf8;"
            #创建班级表
            sql8 = "create table clazz(clazz_number varchar(3) primary key, clazz_name varchar(50) not null, clazz_major varchar(50) not null)charset=utf8;"
            #创建超级管理员
            sql9 = "insert into user values('20180000','SuperAdmin','abcdef',2);"
            self.cur.execute(sql1)
            self.cur.execute(sql2)
            self.cur.execute(sql3)
            self.cur.execute(sql4)
            self.cur.execute(sql5)
            self.cur.execute(sql6)
            self.cur.execute(sql7)
            self.cur.execute(sql8)
            self.cur.execute(sql9)
            self.db.commit()
        except Exception as e:
            pass
    def myclose(self):
        self.cur.close()
        self.db.close()

c = College()
c.myclose()







