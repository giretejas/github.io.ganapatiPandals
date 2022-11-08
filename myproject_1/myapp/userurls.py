from django.urls import path
from . import views

#import myapp.userurls

urlpatterns = [
    path('', views.home,name='index'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('test/', views.test, name='test'),
    path('visual/', views.visual, name='visual'),
    path('userregi/', views.userregi, name='userregi'),
    path('userregipage/', views.userregipage, name='userregipage'),
    path('res/', views.show, name='res'),
    path('kk/', views.login_request, name='kk'),
    path('login/', views.login, name='login'),
    path('adminview/', views.adminview, name='adminview'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('mes/', views.mes, name='mes'),
    path('apm/', views.apm, name='apm'),

]