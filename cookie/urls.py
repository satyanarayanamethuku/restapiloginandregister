from django.conf.urls import url
from .import views
app_name='cookie'
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^insert$',views.insert,name='insert'),
    url(r'^user_login$',views.user_login,name='user_login'),
    url(r'^contact$',views.contact,name='contact'),
]