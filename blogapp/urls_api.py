from django.contrib import admin
from django.urls import path,include
from . import views_api
urlpatterns = [

    path("login/",views_api.Loginview,name ='login_api'),
    path("register/",views_api.Register , name = 'register_api'),
    # path('comment/',views_api.Comment,name = 'comment_api')

]
