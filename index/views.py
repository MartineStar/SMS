from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .modular.islogin import islogin
from .modular.gly import Administrators
from .modular.stu import Studentistrators
from .modular.teacher import Teacher
import json

# Create your views here.


def login_views(request):
    '''登录函数'''
    if request.method == "POST":
        user = request.POST.get("username", None)
        pwd = request.POST.get("passwd", None)
        right_id = request.POST.get('right_id', None)
        # print(user, pwd, right_id)
        administrators_0 = Administrators()
        isInto = administrators_0.check_user(number = user)
        Sbulletin = administrators_0.check_notice()[0][2]
        Tbulletin = administrators_0.check_notice()[0][1]
        if isInto[0][4] == '1':
            if islogin(user, pwd, right_id):
                if (administrators_0.check_student(number=user) == 'none') and (right_id=='0'):
                    data = administrators_0.check_user(number=user)
                    user_id = data[0][0]
                    name = data[0][1]
                    json_data = {'name':name,'user_id':user_id,'Sbulletin':Sbulletin}
                elif (administrators_0.check_teacher(number=user) == 'none') and (right_id=='1'):
                    data = administrators_0.check_user(number=user)
                    user_id = data[0][0]
                    name = data[0][1]
                    json_data = {'name':name,'user_id':user_id,'Tbulletin':Tbulletin}
                else:
                    if right_id == '0':
                        data = administrators_0.check_student(number=user)
                        name = data[0][1]
                        user_id = data[0][0]
                        major_number = data[0][3]
                        class_number = data[0][4]
                        instructor = data[0][5]
                        phone = data[0][6]
                        QQ = data[0][7]
                        if data[0][2] == '0':
                            gender = '男'
                        else:
                            gender = '女'
                        json_data = {'name':name,'user_id':user_id,'gender':gender,
                        'major_number':major_number,'class_number':class_number,'instructor':instructor,
                        'phone':phone,'QQ':QQ,'Sbulletin':Sbulletin}
                    elif right_id == '1':
                        data = administrators_0.check_teacher(number=user)
                        user_id = data[0][0]
                        name = data[0][1]
                        data_birth = data[0][3]
                        major_number = data[0][4]
                        phone = data[0][5]
                        QQ = data[0][6]
                        gender = data[0][2]
                        json_data = {'name':name,'user_id':user_id,'gender':gender,
                        'major_number':major_number,'data_birth':data_birth,'phone':phone,'QQ':QQ,'Tbulletin':Tbulletin}
                if right_id == '0':
                    return render(request, 'Student.html', json_data)
                elif right_id == '1':
                    return render(request, 'Teacher.html', json_data)
                elif right_id == '2':
                    Super = administrators_0.check_user(number=user)
                    json_data = {'name':Super[0][1],'number':Super[0][0]}
                    return render(request ,'admin.html', json_data)
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html')
    return render(request,'login.html')


def login1_views(request):
    '''核对用户名'''
    if request.method == 'POST':
        uName = request.POST['username']
        administrators_0 = Administrators()
        data = administrators_0.check_user(number=uName)
        if data != 'none':
            json_data = {'data':'success'}
        else:
            json_data = {'data':'fail'}
        administrators_0.close()
        return JsonResponse(json_data)

def login2_views(request):
    '''核对密码函数'''
    if request.method == 'POST':
        uPwd = request.POST['password']
        uName = request.POST['username']
        administrators_0 = Administrators()
        data = administrators_0.check_user(number=uName,password=uPwd)
        if data != 'none':
            json_data = {'data':'success'}
        else:
            json_data = {'data':'fail'}
        administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views1(request):
    '''学生列表函数'''
    if request.method == "POST":
        administrators_0 = Administrators()
        data = administrators_0.check_student()
        list_qd = []
        i = 0
        if data != 'none':
            for dt in data:
                bj_lb = administrators_0.check_clazz(name=dt[4])
                grade = bj_lb[0][2]
                if dt[2] == '0':
                    sex = '男'
                else:
                    sex = '女'
                i += 1
                list_qd.append({'id':i,'number':dt[0],'name':dt[1],'sex':sex,'phone':dt[6],'qq':dt[7],'clazz':dt[4],'grade':grade})
        json_data = {"total":i,"rows":list_qd}
        administrators_0.close()
        return JsonResponse(json_data)
    return render(request ,'student_list.html')


def mysrc_views2(request):
    '''教师列表函数'''
    if request.method == "POST":
        administrators_0 = Administrators()
        data = administrators_0.check_teacher()
        list_qd = []
        i = 0
        if data != 'none':
            for dt in data:
                i += 1
                list_qd.append({'tea_number':dt[0],'name':dt[1],'gender':dt[2],'data_birth':dt[3],'phone':dt[5],'qq':dt[6]})
        json_data = {"total":i,"rows":list_qd}
        return JsonResponse(json_data)
    return render(request ,'teacher_list.html')


def mysrc_views3(request):
    '''年级列表函数'''
    return render(request ,'grade_list.html')

def mysrc_views31(request):
    '''增加年级列表'''
    if request.method == "POST":
        data = request.POST
        nj_name = data['vtm_name']
        nj_id = data['vtm_id']
        administrators_0 = Administrators()
        addNj = administrators_0.add_major(nj_id,nj_name)
        if addNj == 'ok':
            json_data = {'data':'success'}
            administrators_0.close()
        else:
            json_data = {'data':'false'}
            administrators_0.close()
        return JsonResponse(json_data)
    else:
        print(request.GET)

def mysrc_views32(request):
    '''查询所有年级函数'''
    administrators_0 = Administrators()
    data = administrators_0.check_major()
    list_qd = []
    i = 0
    if data != 'none':
        for dt in data:
            i += 1
            list_qd.append({'id':dt[0],'name':dt[1]})
    json_data = {"total":i,"rows":list_qd}
    administrators_0.close()
    return JsonResponse(json_data)

def mysrc_views33(request):
    '''删除年级函数，同时把该年级的所有班级和班级里的所有学生和关联成绩等信息删除，慎用！'''
    if request.method == "POST":
        data = request.POST
        del_id = data['gradeid']                                           #要删除的年级的id
        administrators_0 = Administrators()

        DelMajorName = administrators_0.check_major(number=del_id)[0][1]   #要删除的年级的名称
        DEL1 = administrators_0.del_student(major_number=DelMajorName)            #同时把该年级下学生删除
        DEL2 = administrators_0.del_score(maj_name=DelMajorName)                  #同时把该年级成绩删除
        DEL3 = administrators_0.del_m_c(maj_numb=del_id)                          #同时把该年级下专业课和考试删除
        DEL4 = administrators_0.del_exam(maj_numb=DelMajorName)                   #同时把该年级下专业课和考试删除
        DEL5 = administrators_0.del_clazz(clazz_major=DelMajorName)               #同时把该年级下所有的班级删除
        DEL6 = administrators_0.del_major(number=del_id)

        if (DEL1 == 'ok') and (DEL2 == 'ok') and (DEL3 == 'ok') and (DEL4 == 'ok') and (DEL5 == 'ok') and (DEL6 == 'ok'):
            json_data = {'data':'success'}
            administrators_0.close()
            mysrc_views3(request)
        else:
            json_data = {'data':'false'}
            administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views4(request):
    '''班级列表函数,'''
    return render(request ,'clazz_list.html')

def mysrc_views40(request):
    '''年级下拉列表'''
    if request.method == "POST":
        administrators_0 = Administrators()
        data = administrators_0.check_major()
        list_qd = []
        i = 0
        if data != 'none':
            for dt in data:
                i += 1
                list_qd.append({'clazz_name':dt[1]})
        administrators_0.close()
        return HttpResponse(json.dumps(list_qd))
            

def mysrc_views41(request):
    '''增加班级函数'''
    if request.method == "POST":
        data = request.POST  
        number = data['add_id']
        name = data['name']
        clazz_major = data['gradeid']
        administrators_0 = Administrators()
        if name[:-2]==clazz_major:
            if administrators_0.add_clazz(number,name,clazz_major) == 'ok':
                json_data = {'data':'success'}
                administrators_0.close()
            else:
                json_data = {'data':'false'}
                administrators_0.close()
        else:
            json_data = {'data':'None'}
            administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views42(request):
    '''查询所有班级函数'''
    if request.method == "POST":
        sofm = request.POST
        list_qd = []
        i = 0
        administrators_0 = Administrators()
        if 'gradeid' in sofm:
            data = administrators_0.check_clazz(clazz_major=sofm['gradeid'])
        else:
            data = administrators_0.check_clazz()
        if data != 'none':
            for dt in data:
                i += 1
                list_qd.append({'id':dt[0],'name':dt[1],'grade':dt[2]})
        json_data = {"total":i,"rows":list_qd}
        administrators_0.close()
        return JsonResponse(json_data)

def mysrc_views43(request):
    '''删除班级函数'''
    if request.method == "POST":
        data = request.POST
        del_id = data['clazzid']            #要删除班级的id
        administrators_0 = Administrators()

        className = administrators_0.check_clazz(number=del_id)[0][1]       #要删除班级的名字
        DEL1 = administrators_0.del_exam(class_number=className)            #删除班级同时删除考试
        DEL2 = administrators_0.del_student(clazz_name=className)           #删除班级同时删除学生成绩
        DEL3 = administrators_0.del_m_c(cla_numb=className)                 #删除班级同时删除专业课程
        DEL4 = administrators_0.del_student(clazz_name=className)           #删除班级同时删除学生
        DEL5 = administrators_0.del_clazz(number=del_id)                    #删除班级

        if (DEL1 == 'ok') and (DEL2 == 'ok') and (DEL3 == 'ok') and (DEL4 == 'ok') and (DEL5 == 'ok'):
            json_data = {'data':'success'}
        else:
            json_data = {'data':'false'}
        administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views5(request):
    '''课程列表函数'''
    return render(request ,'course_list.html')

def mysrc_views51(request):
    '''增加课程函数'''
    if request.method == "POST":
        data = request.POST
        clazz_number = data['class_number']         # 班级
        course_number = data['course_number']       # 课程
        major_number = data['major_number']         # 专业代码
        course_place = data['course_place']         #　课室
        course_day = data['course_day']             # 日期
        course_time = data['course_time']           # 时间
        tea_number = '待定'                         # 上课老师
        course_interval = data['course_interval']   # 课时
        course_week = '星期'+data['course_week']      # 周几
        administrators_0 = Administrators()
        is_users = administrators_0.check_clazz(clazz_major=major_number)
        L = []
        if is_users != 'none':                                     # 用来存储所有班级的临时空间列表
            for is_user in is_users:
                L.append(is_user[1])

        if (administrators_0.check_major(name=major_number) != 'none') and (clazz_number in L):
            add_kc = administrators_0.add_m_c(maj_numb=major_number, cou_numb=course_number,cla_numb=clazz_number, tea_numb=tea_number, place=course_place,day=course_day, time=course_time,week=course_week,date=course_interval)
            if add_kc == 'ok':
                json_data = {'data':'success'}
            else:
                json_data = {'data':'false'}
        else:
            json_data = {'data':'false'}
        administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views52(request):
    '''查询所有课程函数'''
    administrators_0 = Administrators()
    data = administrators_0.check_m_c()
    list_qd = []
    i = 0
    if data != 'none':
        for dt in data:
            i += 1
            list_qd.append({'id':dt[0],'course_number':dt[2],'major_number':dt[1],'class_number':dt[3],'teach_number':dt[4],'course_place':dt[5],'course_day':dt[6],'course_time':dt[7],'course_week':dt[8],'course_interval':dt[9]})
    json_data = {"total":i,"rows":list_qd}
    administrators_0.close()
    return JsonResponse(json_data)

def mysrc_views53(request):
    '''删除课程函数'''
    if request.method == "POST":
        data = request.POST
        administrators_0 = Administrators()

        del_id = data['courseid']               #要删除课程的id

        if administrators_0.del_m_c(id=del_id) == 'ok':
            json_data = {'data':'success'}
            administrators_0.close()
        else:
            json_data = {'data':'false'}
            administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views6(request):
    '''考试列表处理函数'''
    return render(request, 'exam_list.html')

def mysrc_views61(request):
    '''管理员增加考试函数'''
    if request.method == "POST":
        data = request.POST
        # print(data)
        Uname = data['Uname']
        Sname = data['Sname']
        type = data['type']
        etime = data['etime']
        class_number = data['gradeid']
        remark = data['remark']
        administrators_0 = Administrators()
        L = []
        Courses = administrators_0.check_m_c(cla_numb=class_number)
        if Courses != 'none':
            for course in Courses:
                L.append(course[2])
        if (administrators_0.check_m_c(cou_numb=Sname) != 'none') and (Sname in L):
            major_name = administrators_0.check_clazz(name=class_number)[0][2]
            sofm = administrators_0.add_exam(term=Uname,maj_numb=major_name,class_number=class_number,course_name=Sname,e_place=type,e_day=etime,e_time=remark)
            if sofm == 'ok':
                json_data = {'data':'success'}
            else:
                json_data = {'data':'false'}
        else:
            json_data = {'data':'null'}
        administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views62(request):
    '''管理员查看考试函数'''
    administrators_0 = Administrators()
    list_qd = []
    i = 0
    sofm = request.POST
    if 'gradeid' in sofm:
        data = administrators_0.check_exam(maj_numb=sofm['gradeid'])
    elif 'clazzid' in sofm:
        data = administrators_0.check_exam(class_number=sofm['clazzid'])
    else:
        data = administrators_0.check_exam()
    if data != 'none':
        for dt in data:
            i += 1
            list_qd.append({'id':dt[0],'name':dt[1],'etime':dt[6],'type':dt[5],'grade':dt[2],'clazz':dt[3],'course':dt[4],'remark':dt[7]})
    json_data = {"total":i,"rows":list_qd}
    # print(json_data)
    administrators_0.close()
    return JsonResponse(json_data)

def mysrc_views63(request):
    '''管理员删除考试函数'''
    if request.method == "POST":
        data = request.POST
        del_id = data['id']
        administrators_0 = Administrators()
        sofm = administrators_0.del_exam(ID=del_id)
        if sofm == 'ok':
            json_data = {'data':'success'}
        else:
            json_data = {'data':'false'}
        administrators_0.close()
        return JsonResponse(json_data)



def mysrc_views64(request):
    '''班级下拉列表'''
    if request.method == "POST":
        data = request.POST
        # print('调用年级',data)
        administrators_0 = Administrators()
        data = administrators_0.check_major()
        list_qd = []
        i = 0
        if data != 'none':
            for dt in data:
                i += 1
                list_qd.append({'clazz_name':dt[1]})
        administrators_0.close()
        return HttpResponse(json.dumps(list_qd))

def mysrc_views65(request):
    '''年级下拉列表'''
    if request.method == "POST":
        sofm = request.POST
        administrators_0 = Administrators()
        if 'gradeid' in sofm:
            data = administrators_0.check_clazz(clazz_major=sofm['gradeid'])
        else:
            data = administrators_0.check_clazz()
        list_qd = []
        i = 0
        if data != 'none':
            for dt in data:
                i += 1
                list_qd.append({'clazz_name':dt[1]})
        administrators_0.close()
        return HttpResponse(json.dumps(list_qd))

def mysrc_views66(request):
    if request.method == "POST":
        sofm = request.POST
        examID = sofm['id']
        list_qd = []
        i = 0
        administrators_0 = Administrators()
        data = administrators_0.check_exam(ID = examID)
        Scores = administrators_0.check_score(cla_numb=data[0][3],cou_numb=data[0][4])
        for score in Scores:
            i += 1
            list_qd.append({'number':score[4],'name':score[1],'course':score[5],'clazz':score[3],'score':score[6]})
        json_data = {'total':i,'rows':list_qd}
        return JsonResponse(json_data)
    else:
        sofm = request.GET
        print('调用了66函数GET',sofm)



def mysrc_views7(request):
    '''用户信息的处理函数'''
    return render(request, 'add_user.html')

def mysrc_views71(request):
    '''添加添加用户信息的处理函数'''
    if request.method == "POST":
        data = request.POST
        # print(data)
        user_number = data['user_number']
        type = data['value']
        name = data['name']
        administrators_0 = Administrators()
        if data['value'] == '0':
            nub_data = administrators_0.check_clazz(name=user_number[:-2])
            if (nub_data != 'none') and (nub_data != 'false'):
                isdata = administrators_0.add_user(user_number,name,type)
                if isdata == 'ok':
                    json_data = {'data':'success'}
                else:
                    json_data = {'data':'false'}
            else:
                json_data = {'data':'false'}
        else:
            isdata = administrators_0.add_user(user_number,name,type)
            if isdata == 'ok':
                json_data = {'data':'success'}
            else:
                json_data = {'data':'false'}
        administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views72(request):
    '''获取所有用户的信息'''
    administrators_0 = Administrators()
    data = administrators_0.check_user(mytype=0)
    list_qd = []
    i = 0
    if data != 'none':
        # print(data)
        for dt in data:
            i += 1
            list_qd.append({'user_id':dt[0],'user_name':dt[1],'user_password':dt[2],'user_typeid':'学生'})
    data = administrators_0.check_user(mytype=1)
    if data != 'none':
        # print(data)
        for dt in data:
            i += 1
            list_qd.append({'user_id':dt[0],'user_name':dt[1],'user_password':dt[2],'user_typeid':'教师'})
    json_data = {"total":i,"rows":list_qd}
    # print(json_data)
    administrators_0.close()
    return JsonResponse(json_data)

def mysrc_views73(request):
    '''删除用户函数'''
    if request.method == "POST":
        data = request.POST
        del_id = data['gradeid']
        administrators_0 = Administrators()
        if administrators_0.del_user(number=del_id) == 'ok':
            json_data = {'data':'success'}
            administrators_0.close()
            # mysrc_views5(request)
        else:
            json_data = {'data':'false'}
            administrators_0.close()
        return JsonResponse(json_data)


def mysrc_views8(request):
    '''系统设置'''
    if request.method == "POST":
        administrators_0 = Administrators()
        if request.POST['name'] in 'forbidTeacher':
            if request.POST['value'] == '1':
                cp = administrators_0.update_isActive(type=1,isActive=0)
            else:
                cp = administrators_0.update_isActive(type=1,isActive=1)
        elif request.POST['name'] in 'forbidStudent':
            if request.POST['value'] == '1':
                cp = administrators_0.update_isActive(type=0,isActive=0)
            else:
                cp = administrators_0.update_isActive(type=0,isActive=1)
        elif request.POST['name'] in 'schoolName':
            data = request.POST['value']
            cp = administrators_0.update_notice(schoolname=data)
        elif request.POST['name'] in 'noticeTeacher':
            data = request.POST['value']
            cp = administrators_0.update_notice(teacherBulletin=data)           
        elif request.POST['name'] in 'noticeStudent':
            data = request.POST['value']
            cp = administrators_0.update_notice(studentBulletin=data)
        if cp == 'ok':
            json_data = {'data':'success'}
        else:
            json_data = {'data':'false'}
        administrators_0.close()
        return JsonResponse(json_data)            
    else:
        administrators_0 = Administrators()
        data = administrators_0.check_notice()[0]
        schoolname = data[0]
        teacherBulletin = data[1]
        studentBulletin = data[2]
        json_data = {'schoolname':schoolname,'teacherBulletin':teacherBulletin,'studentBulletin':studentBulletin}
        return render(request, 'admin_personal.html', json_data)

def mysrc_views81(request):
    '''管理员修改密码'''
    if request.method == 'POST':
        data = request.POST
        oldpwd = data['oldpwd']
        newpwd = data['newpwd']
        number = data['number']
        administrators_0 = Administrators()
        data = administrators_0.check_user(number=number,password=oldpwd)
        if data != 'none':
            NewPwd = administrators_0.update_user(number=number,new_pwd=newpwd)
            if NewPwd == 'ok':
                json_data = {'data':'success'}
            else:
                json_data = {'data':'no'}
        else:
            json_data = {'data':'false'}
        return JsonResponse(json_data)




def mysrc_a1(request):
    '''班级通讯录'''
    if request.method == "POST":
        is_class_number = request.POST['order']
        administrators_1 = Administrators()
        data = administrators_1.check_student(class_number=is_class_number)
        list_qd = []
        i = 0
        if data != 'none':
            for dt in data:
                i += 1
                bj_lb = administrators_1.check_clazz(name=dt[4])
                major_number = bj_lb[0][2]
                if dt[2] == '0':
                    gender = '男'
                else:
                    gender = '女'
                list_qd.append({'number':dt[0],'name':dt[1],'gender':gender,'class_number':dt[4],'major_number':major_number,'instructor':dt[5],'phone':dt[6],'qq':dt[7]})
        json_data = {"total":i,"rows":list_qd}
        return JsonResponse(json_data)

    return render(request, 'Student_noteList.html')

def mysrc_a2(request):
    '''更改个人信息'''
    if request.method == "POST":
        data = request.POST
        QQ1 = data['qq']
        number1 = data['number']
        sex1 = data['sex']
        name1 = data['name']
        phone1 = data['phone']
        if sex1 == '男':
            sex1 = 0
        else:
            sex1 = 1
        administrators_1 = Administrators()
        studentistrators_1 = Studentistrators()
        data = administrators_1.check_student(number=number1)
        if data != 'none':
            if studentistrators_1.update_student(number=number1,gender=sex1,phone=phone1,QQ=QQ1) == 'ok':
                json_data = {'data':'success'}
            else:
                json_data = {'data':'false'}
        else:
            besc = studentistrators_1.add_student(number=number1,name=name1,gender=sex1,phone=phone1,QQ=QQ1,instructor='Null')
            if besc == 'ok':
                json_data = {'data':'success'}
            else:
                json_data = {'data':'false'}
        return JsonResponse(json_data)
    return render(request, 'Student_personal.html', )

def mysrc_a3(request):
    '''学生成绩页面'''
    return render(request, 'Student_exam.html')

def mysrc_a4(request, num):
    '''通过学生学号查询成绩函数'''
    administrators_1 = Administrators()
    data = administrators_1.check_score(stu_numb=num)
    list_qd = []
    i = 0
    if data != 'none':
        for dt in data:
            i += 1
            list_qd.append({'id':dt[0],'term':dt[1],'major_number':dt[2],'class_number':dt[3],'stu_number':dt[4],'course_number':dt[5],'score':dt[6]})
    else:
        print("该学生目前没有成绩")
    json_data = {"total":i,"rows":list_qd}
    administrators_1.close()
    return JsonResponse(json_data)

def mysrc_a5(request):
    '''修改学生密码函数'''
    if request.method == "POST":
        data = request.POST
        oldpwd = data['oldpwd']
        newpwd = data['newpwd']
        user_id = data['user_id']
        administrators_1 = Administrators()
        data = administrators_1.check_user(number=user_id,password=oldpwd)
        if data != 'none':
            if administrators_1.update_user(number=user_id,new_pwd=newpwd) == 'ok':
                json_data = {"data":'success'}
            else:
                json_data = {"data":'false'}
        else:
            json_data = {"data":'false'}
        administrators_1.close()
        return JsonResponse(json_data)

def mysrc_a6(request):
    '''学生查看课程信息'''
    if request.method == "POST":
        print(request.POST)
        className = request.POST['class_number']
        administrators_1 = Administrators()
        data = administrators_1.check_m_c(cla_numb=className)
        list_qd = []
        i = 0
        if data != 'none':
            for dt in data:
                i += 1
                list_qd.append({'id':dt[0],'course_number':dt[2],'major_number':dt[1],'class_number':dt[3],'teach_number':dt[4],'course_place':dt[5],'course_day':dt[6],'course_time':dt[7],'course_week':dt[8],'course_interval':dt[9]})
        json_data = {"total":i,"rows":list_qd}
        administrators_1.close()
        return JsonResponse(json_data)
    return render(request, 'Student_course.html')


def mysrc_t1(request):
    '''教师通讯录'''
    if request.method == 'POST':
        administrators_2 = Administrators()
        data = administrators_2.check_teacher()
        list_qd = []
        i = 0
        if data != 'none':
            for dt in data:
                i += 1
                list_qd.append({'tea_number':dt[0],'name':dt[1],'gender':dt[2],'data_birth':dt[3],'phone':dt[5],'qq':dt[6]})
        json_data = {"total":i,"rows":list_qd}
        administrators_2.close()
        return JsonResponse(json_data)
    return render(request,'Teacher_noteList.html')


def mysrc_t2(request):
    '''更改个人信息'''
    if request.method == "POST":
        data = request.POST
        QQ1 = data['qq']
        number1 = data['tea_number']
        sex1 = data['gender']
        name1 = data['name']
        phone1 = data['phone']
        data_birth1 = data['data_birth']
        administrators_2 = Administrators()
        teacher_1 = Teacher()
        data = administrators_2.check_teacher(number=number1)
        if data != 'none':
            AddTeacher = teacher_1.update_teacher(number=number1,gender=sex1,data_birth=data_birth1,phone=phone1,QQ=QQ1)
            if AddTeacher == 'ok':
                json_data = {'data':'True'}
            else:
                json_data = {'data':'false'}
        else:
            besc = teacher_1.add_teacher(tea_number=number1,name=name1,gender=sex1,data_birth=data_birth1,phone=phone1,QQ=QQ1,major_number='Null')
            if besc == 'ok':
                json_data = {'data':'True'}
            else:
                json_data = {'data':'false'}
        # print(besc)
        administrators_2.close()
        return JsonResponse(json_data)

    return render(request,'Teacher_personal.html')

def mysrc_t3(request):
    '''考试列表'''
    if request.method == 'POST':
        list_qd = []
        i = 0
        administrators_2 = Administrators()
        data = administrators_2.check_exam()
        if data != 'none':
            for dt in data:
                i += 1
                number = dt[0]
                exam_name = dt[1]
                course_number = dt[4]
                exam_time = dt[6]
                exam_interval = dt[7][5:]
                class_number = dt[3]
                major_number = dt[2]
                term = '年级统考'
                list_qd.append({'id':number,'exam_name':exam_name,
                    'course_number':course_number,'exam_time':exam_time,
                    'exam_interval':exam_interval,'class_number':class_number,
                    'major_number':major_number,'term':term})
        json_data = {"total":i,"rows":list_qd}
        administrators_2.close()
        return JsonResponse(json_data)
    else:
        print('GET',request.GET)
        return render(request,'Teacher_examList.html')

def mysrc_t4(request):
    '''获取考生信息用来添加成绩'''
    if request.method == 'POST':
        list_qd = []
        administrators_2 = Administrators()
        if 'class_number' in request.POST:
            sofm = administrators_2.check_exam(ID=request.POST['class_number'])
            class_number = request.POST['class_number']
            data = administrators_2.check_student(class_number=sofm[0][3])
            for dt in data:
                number = dt[0]
                name = dt[1]
                list_qd.append({'number':number,'name':name,'score':'0','course':request.POST['course']})
        administrators_2.close()
        return HttpResponse(json.dumps(list_qd))
    else:
        print('GET',request.GET)
        return JsonResponse({'data':'0'})

def mysrc_t41(request):
    '''班级下拉列表,多余了'''
    if request.method == "POST":
        list_qd = []
        administrators_2 = Administrators()
        data = administrators_2.check_clazz()
        for dt in data:
            list_qd.append({'clazz_name':'添加或修改'})
        list_qd = [{'clazz_name':'刷新列表'}]
        return HttpResponse(json.dumps(list_qd))

def mysrc_t42(request):
    '''查看成绩'''
    if request.method == "POST":
        data = request.POST
        exam_clazz = data['class']              #班级
        exam_course = data['course']          #课程
        administrators_2 = Administrators()
        TScores = administrators_2.check_score(cla_numb=exam_clazz,cou_numb=exam_course)
        list_qd = []
        i = 0
        if TScores != 'none':
            for TScore in TScores:
                i += 1
                list_qd.append({'stu_number':TScore[4],'stu_name':TScore[1],'course_number':TScore[5],'score':TScore[6]})
        json_data = {"total":i,"rows":list_qd}
        administrators_2.close()
        return JsonResponse(json_data)
    else:
        print('调用了t42A',request.GET)

def mysrc_t43(request):
    '''添加成绩或修改成绩'''
    if request.method == 'POST':
        data = request.POST
        administrators_2 = Administrators()
        for dt in data:
            for D in eval(dt):
                number1 = D['number']    #学号
                course1 = D['course']    #课程
                name1 = D['name']        #姓名
                score1 = D['score']      #分数
                clazzStudent = administrators_2.check_student(name=name1)[0][4]
                sofm = administrators_2.check_m_c(cou_numb=course1)
                for sf in sofm:
                    if sf[3] in clazzStudent:
                        class_number1 = sf[3]   #班级
                        major_name = administrators_2.check_clazz(name=class_number1)[0][2]      #年级
                        courseId1 = sf[0]   #课程id
                if  administrators_2.check_score(cla_numb=class_number1,cou_numb=course1,stu_numb=number1) != 'none':
                    addScore = administrators_2.update_score(cla_numb=class_number1,stu_numb=number1,course_number=course1,new_score=score1)
                else:
                    addScore = administrators_2.add_score(term=name1,major_number=courseId1,cla_numb=class_number1,stu_numb=number1,cou_numb=course1,score=score1,maj_name=major_name)
                if addScore == 'ok':
                    json_data = {'data':'success'}
                else:
                    json_data = {'data':'0'}
    return JsonResponse(json_data)

def mysrc_t44(request):
    '''课程下拉列表'''
    if request.method == 'POST':
        administrators_2 = Administrators()
        list_qd = []
        if 'class_number' in request.POST:
            sofm = administrators_2.check_score(cla_numb=request.POST['class_number'],cou_numb=request.POST['clazz'])
            data = administrators_2.check_student(class_number=request.POST['class_number'])
            if sofm != 'none':
                for sf in sofm:
                    number = sf[4]
                    name = sf[1]
                    score = sf[6]
                    course = sf[5]
                    list_qd.append({'number':number,'name':name,'score':score,'course':course})
            else:
                for dt in data:
                    number = dt[0]
                    name = dt[1]
                    list_qd.append({'number':number,'name':name,'score':'0','course':request.POST['clazz']})
        administrators_2.close()
        json_data = {"total":'20',"rows":list_qd}
        return JsonResponse(json_data)

def mysrc_t5(request):
    '''教师修改密码'''
    if request.method == "POST":
        data = request.POST
        oldpwd = data['oldpwd']
        newpwd = data['newpwd']
        user_id = data['user_id']
        administrators_1 = Administrators()
        data = administrators_1.check_user(number=user_id,password=oldpwd)
        if data != 'none':
            if administrators_1.update_user(number=user_id,new_pwd=newpwd) == 'ok':
                json_data = {"data":'success'}
            else:
                json_data = {"data":'false'}
        else:
            json_data = {"data":'false'}
        administrators_1.close()
        return JsonResponse(json_data)

