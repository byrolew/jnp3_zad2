from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.menu, name="menu"),
    url(r'^pe/$', views.pe, name="pe"),
    url(r'^welcome/$', views.welcome, name="welcome"),
    url(r'^instr_gil/$', views.instr_gil, name="instr_gil"),
    url(r'^instr_cards/$', views.instr_cards, name="instr_cards"),
    url(r'^instr_test_gil/$', views.instr_test_gil, name="instr_test_gil"),
    url(r'^task_number/$', views.task_number, name="task_number"),
    url(r'^task2/$', views.task2, name="task2"),
    url(r'^task1/$', views.task1, name="task1"),
    url(r'^task_test/$', views.task_test, name="task_test"),
    url(r'^gil_train/$', views.gil_train, name="gil_train"),
    url(r'^gil_test/$', views.gil_test, name="gil_test"),
    url(r'^sex_age/$', views.sex_age, name="sex_age"),
    url(r'^report.csv$', views.report, name="report"),
]
