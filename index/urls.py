from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles


urlpatterns = [
    # 登录url和获取登录信息
    url(r'^$', login_views, name = 'login'),
    url(r'^islogin_name/$', login1_views, name = 'islogin_name'),
    url(r'^islogin_pwd/$', login2_views, name = 'islogin_pwd'),
    # 管理员url
    # 1开头函数处理学生信息
    url(r'^asdfdsfsfsdfa/$', mysrc_views1, name='mysrc_stu'),
    # url(r'^asdfdsfsfsdfa/stulb_durl/$', mysrc_views11, name='mysrc_stu_list'),

    # 2开头函数处理教师信息
    url(r'^aksdjfsaldjkf/$', mysrc_views2, name='mysrc_teach'),

    # 3开头的函数处理年级信息
    url(r'^ksajdfoiwekaj/$', mysrc_views3, name='mysrc_grade'),
    url(r'^ksajdfoiwekaj/ajax_submit/$', mysrc_views31, name='mysrc_grade_ajax_submit'),
    url(r'^ksajdfoiwekaj/njlb_durl/$', mysrc_views32, name='mysrc_grade_list'),
    url(r'^ksajdfoiwekaj/njsc_durl/$', mysrc_views33, name='mysrc_grade_del'),

    # 4开头的函数处理班级信息
    url(r'^eqwrqroiwekaj/$', mysrc_views4, name='mysrc_clazz'),
    url(r'^eqwrqroiwekaj/bj_xllb/$', mysrc_views40, name='mysrc_clazz_xl'),
    url(r'^eqwrqroiwekaj/ajax_submit/$', mysrc_views41, name='mysrc_clazz_ajax_submit'),
    url(r'^eqwrqroiwekaj/bjlb_durl/$', mysrc_views42, name='mysrc_clazz_list'),
    url(r'^eqwrqroiwekaj/bjsc_durl/$', mysrc_views43, name='mysrc_clazz_del'),

    # 5开头的函数处理课程
    url(r'^qwsadfsdwekaj/$', mysrc_views5, name='mysrc_course'),
    url(r'^qwsadfsdwekaj/ajax_submit/$', mysrc_views51, name='mysrc_course_ajax_submit'),
    url(r'^qwsadfsdwekaj/kclb_durl/$', mysrc_views52, name='mysrc_course_list'),
    url(r'^qwsadfsdwekaj/kcsc_durl/$', mysrc_views53, name='mysrc_course_del'),

    # 6考试列表处理函数
    url(r'^haheiiiioadkj/$', mysrc_views6, name='mysrc_exam'),
    url(r'^haheiiiioadkj/add_ks_submit/$', mysrc_views61, name='mysrc_exam_add_submit'),    #增加考试
    url(r'^haheiiiioadkj/kslb_durl/$', mysrc_views62, name='mysrc_exam_list'),              #查看考试
    url(r'^haheiiiioadkj/kslb_del_durl/$', mysrc_views63, name='mysrc_exam_del'),           #删除考试
    url(r'^haheiiiioadkj/ksnj_xllb/$', mysrc_views64, name='mysrc_exam_ksnj_xllb'),         #年级下拉列表
    url(r'^haheiiiioadkj/ksbj_xllb/$', mysrc_views65, name='mysrc_exam_ksbj_xllb'),         #班级下拉列表
    url(r'^haheiiiioadkj/score_exam/$', mysrc_views66, name='score_exam'),                #成绩统计

    # 7添加用户信息的处理函数
    url(r'^hehwedfiiodl/$', mysrc_views7, name='add_user'),
    url(r'^hehwedfiiodl/add_user_submit/$', mysrc_views71, name='add_user_ajax_submit'),
    url(r'^hehwedfiiodl/cx_user_durl/$', mysrc_views72, name='add_user_list'),
    url(r'^hehwedfiiodl/sc_user_durl/$', mysrc_views73, name='add_user_del'),

    #　8系统设置
    url(r'^hettttdfiiodl/$', mysrc_views8, name='user_s'),
    url(r'^hettttdfiiodl/updata_password/$', mysrc_views81, name='admin_password'),
]


# 学生url
urlpatterns += [
    url(r'^iasdkfjopiuu/$', mysrc_a1, name='student_bjtxl'),
    url(r'^iasdkfjopiuu/updata_student/$', mysrc_a2, name='student_updata'),
    url(r'^iasdkfjopiuu/cx_student_score/$', mysrc_a3, name='student_score'),
    url(r'^iasdkfjopiuu/cx_student_score_1/(.*)', mysrc_a4, name='student_score_1'),
    url(r'^iasdkfjopiuu/updata_password/$', mysrc_a5, name='student_password'),
    url(r'^iasdkfjopiuu/kclb_student/$', mysrc_a6, name='kclb_student'),
]

# 教师url
urlpatterns += [
    url(r'^isojtasklktf/$', mysrc_t1, name='teacher_jstxl'),
    url(r'^isojtasklktf/updata_teacher/$', mysrc_t2, name='updata_teacher'),
    url(r'^isojtasklktf/exam_teacher/$', mysrc_t3, name='exam_teacher'),                #考试列表
    url(r'^isojtasklktf/dj_exam_teacher/$', mysrc_t4, name='dj_exam_teacher'),          #获取考生信息用来添加成绩
    url(r'^isojtasklktf/bjll_exam_teacher/$', mysrc_t41, name='bjll_exam_teacher'),      #班级下拉列表
    url(r'^isojtasklktf/nte_exam_teacher/$', mysrc_t42, name='nte_exam_teacher'),       #查看成绩
    url(r'^isojtasklktf/student_exam_teacher/$', mysrc_t43, name='student_exam_teacher'),   #添加成绩
    url(r'^isojtasklktf/teacher_coures/$',mysrc_t44,name='teacher_coures'),             #课程下拉列表
    url(r'^isojtasklktf/updata_password/$', mysrc_t5, name='teacher_password'),         #修改密码
]
