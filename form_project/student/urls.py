from django.urls import path
from . import views
urlpatterns=[
    path('',views.student_form, name='student_form'),
    path('student_list',views.student_list,name='student_list')
]