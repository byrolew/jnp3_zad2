from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page, name="login_page"),
    url(r'^form1/$', views.form1, name="form1"),
    url(r'^form2/$', views.form2, name="form2"),
    url(r'^desc/$', views.desc, name="desc"),
    url(r'^end_trial/$', views.end_trial, name="end_trial"),
    url(r'^experiment/$', views.experiment_page, name="experiment_page"),
    url(r'^end_of_session/$', views.end_of_session, name="end_of_session"),
    url(r'^end/$', views.end, name="end"),
    url(r'^reset/$', views.reset, name="reset"),
    url(r'^report.csv$', views.report, name="report"),
    url(r'^panel_admin$', views.panel_admin, name="panel_admin"),
]
