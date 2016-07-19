from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

# user_obj = auth()

urlpatterns = [
    url(r'^$',views.index),
    url(r'^cash/$', views.pay_by_cash),
    url(r'^articles/([0-9]{4})/$', views.year_archive, {'type':'json'}),#默认参数
]