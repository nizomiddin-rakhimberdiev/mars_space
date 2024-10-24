from django.urls import  path

from users.views import login_view, admin_page, add_student, logout_view

urlpatterns = [
    path('', admin_page, name='admin_page'),
    path('login/', login_view, name='login'),
    path('add_student/', add_student, name='add_student'),
    path('logout/', logout_view, name='logout'),
]