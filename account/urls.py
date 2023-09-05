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
    path('gestion',views.gestion,name='gestion'),
    path('rappstas',views.rappstas,name='rappstas'),
    path('securité',views.securité,name='securité'),
    path('surveil',views.surveil,name='surveil'),
    path('etatdedem',views.etatdedem,name='etatdedem'),
    path('info',views.info,name='info'),
    path('notif',views.notif,name='notif'),
    path('prodem',views.prodem,name='prodem'),
    path('assistance',views.assistance,name='assistance'),
    path('connaissance',views.connaissance,name='connaissance'),
    path('demand',views.demand,name='demand'),
    path('redirection',views.redirection,name='redirection'),
    path('comm',views.comm,name='comm'),
    path('GPI',views.GPI,name='GPI'),
    path('GTA',views.GTA,name='GTA'),
    path('ticket',views.ticket,name='ticket'),



]
