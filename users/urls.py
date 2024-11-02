from django.urls import  path

from users.views import login_view, admin_page, add_student, logout_view, add_teacher, add_course, add_group, \
    teachers_view, edit_teacher_view

urlpatterns = [
    path('', admin_page, name='admin_page'),
    path('login/', login_view, name='login'),
    path('add_student/', add_student, name='add_student'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('add_course/', add_course, name='add_course'),
    path('add_group/', add_group, name='add_group'),
    path('logout/', logout_view, name='logout'),
    path('teachers/', teachers_view, name='teachers'),
    path('edit-teacher/<int:id>/', edit_teacher_view, name='edit_teacher')
]