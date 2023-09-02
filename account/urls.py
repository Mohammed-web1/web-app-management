from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', views.login),
    # path('',views.login , name='login'),

    path('tech',views.tech , name='tech'),
    path('help_desk',views.help_desk , name='help_desk'),
    path('employer',views.employer , name='employer'),
    path('admin',views.admin , name='admin'),
    path('register',views.register , name='register'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    #path('',auth_views.LoginView.as_view(template_name='index/index.html'),name='login'),
    path('',views.MyLoginView.as_view(template_name='index/index.html'),name='login'),


]
