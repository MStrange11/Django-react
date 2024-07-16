from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('g-stu/<id>/',StudentGeneric2.as_view()),
    path('g-stu/',StudentGeneric.as_view()),

    path('stu/',StudentAPI.as_view()),
    path('register/',RegisterUser.as_view()),

    # path('', home),
    # path('stu/', post_student),
    # path('stu-upd/<id>/', update_student),
    # path('stu-del/<id>/', delete_student),
    # path('books/', get_book),
]
