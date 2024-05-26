from django.urls import path
from . import views
urlpatterns=[
    path('addEmployee/',views.addEmployee,name='addEmployee'),
    path('addrnd/',views.addrnd,name='addrnd'),
    path('delemployee/<int:pk>/', views.delemployee, name='delemployee'),
    path('employee_list/',views.employee_list,name='employee_list'),
    path('delrnd/<int:pk>/', views.delrnd, name='delrnd'),
    path('rnd_list/',views.rnd_list,name='rnd_list'),

]