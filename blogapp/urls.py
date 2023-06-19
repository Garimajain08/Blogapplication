from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("home/",views.home,name = 'home'),
    path ('froala_editor/', include ('froala_editor.urls')),
    path("login/" ,views.login,name = 'login'),
    path('register/',views.register,name = 'register'),
    path('forget/', views.forget,name='forget'),
    path ( 'comment/<slug>/', views.comment, name='comment' ),
    path('addblogs/',views.addblog,name = 'addblog'),
    path('viewpage/<slug>/',views.viewpage,name = 'viewpage'),
    path('seeblog/',views.seeblogs,name = 'seeblog'),
    path('delete/<id>',views.delete,name = 'delete'),
    path('update/<slug>/',views.update,name ='update'),
    path("logout/",views.logout_view,name='logout'),
    path("verify/<token>/",views.verify,name = 'verify'),

    path('search/',views.search,name='search'),
]
