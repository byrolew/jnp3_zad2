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
    url(r'^task/$', views.task, name="task"),
]
