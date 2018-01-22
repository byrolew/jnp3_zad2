from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.menu, name="menu"),
    url(r'^pe/$', views.pe, name="pe"),
]
