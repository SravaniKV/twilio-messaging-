from django.conf.urls import url
from . import views
#from django.urls import path
from .views import SendSmsCreateView

app_name ='home'

urlpatterns = [
    #twilio
    #url(regex=r'^communication/send/sms/$',view=SendSmsCreateView.as_view(),name='send_sms'),
    url(r'^communication/send/sms/$', views.SendSmsCreateView.as_view(), name='send_sms'),
    #twilio end
    url(r'^$', views.home, name='base'),
    url(r'^searchemp/$', views.searchemp, name='searchemp'),
    url(r'^searchment/$', views.searchment, name='searchment'),
    url(r'^home/$', views.home, name='base'),
    url(r'^base/$', views.home, name='base'),
   #url(r'^home/$', include('omk.urls')),
    url(r'^about/$', views.about, name='about'),
    url(r'^mentor/$', views.mentor, name='mentor'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^index/$', views.index, name='index'),
    url(r'^empindex/$', views.empindex, name='empindex'),
    url(r'^emphome/$', views.emphome, name='emphome'),
    url(r'^mentorhome/$', views.mentorhome, name='mentorhome'),
    url(r'^markattendance/$', views.markattendance, name='markattendance'),
    url(r'^markattendanceedit/$', views.mrkatt_new, name='mrkatt_new'),
    url(r'^studentsreports/$', views.Student_Report, name='studentsreports'),
    url(r'^studentsreportsedit/(?P<pk>\d+)/edit/$', views.Student_Report_Edit, name='Student_Report_Edit'),
    url(r'^createappointments/$', views.createappointments, name='createappointments'),
    url(r'^mentortask/$', views.mentortask, name='mentortask'),
    url(r'^empmarkattendance/$', views.empmarkattendance, name='empmarkattendance'),
    url(r'^empstudentsreports/$', views.Emp_Student_Report, name='empstudentsreports'),
    url(r'^empstudreportedit/(?P<pk>\d+)/edit/$', views.Emp_Student_Report_Edit, name='Emp_Student_Report_Edit'),
    url(r'^empcreateappointments/$', views.empcreateappointments, name='empcreateappointments'),
    url(r'^mentorlist/$', views.mentor_list, name='mentorlist'),
    url(r'^mentoredit/(?P<pk>\d+)/edit/$', views.mentor_edit, name='mentor_edit'),
    url(r'^emptask/$', views.emptask, name='emptask'),
    url(r'^mentorlist/$', views.mentor_list, name='mentorlist'),
    url(r'^mentornew/$', views.mentor_new, name='mentor_new'),
    url(r'^studentlist/$', views.Student_list, name='studentlist'),
    url(r'^mentstudlist/$', views.mentstudlist, name='mentstudlist'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.studentedit, name='studentedit'),
    url(r'^studentsarchive/$', views.studentsarchive, name='studentsarchive'),
    url(r'^studentadd/$', views.studentadd, name='studentadd'),
    url(r'^archive/$', views.archive, name='archive'),

        ]
