import random
from pyexpat.errors import messages
from sqlite3 import connect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from users.forms import AddStudentForm, AddTeacherForm, AddCourseForm, AddGroupForm, EditTeacherForm
from users.models import Student, Teacher, Course


# Create your views here.


def admin_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            students = Student.objects.all().order_by('-date_joined')
            context = {'students': students}
            return render(request, 'admin_page.html', context)
        else:
            student = Student.objects.get(id=request.user.id)
            context = {
                'student': student
            }
            return render(request, 'dashboard.html', context)

    else:
        return redirect('login')


def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            group = form.cleaned_data['group']
            username = str(random.randint(100000, 999999))
            password = str(random.randint(10000, 99999))
            print(first_name, last_name, username, password)
            with open('students.txt', 'a') as f:
                f.write(f"{first_name}, {last_name}, {username}, {password}, {group}")
            user = Student.objects.create_user(first_name=first_name, last_name=last_name, phone=phone, group=group, username=username, password=password)  # Parolni hash qilish
            user.set_password(password)
            user.save()
            # form.save()
            return redirect('admin_page')
    else:
        form = AddStudentForm()  # Re-render form with errors if not valid
    return render(request, 'add_student.html', {'form': form})


def add_teacher(request):
    if request.method == 'POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            username = phone
            password = f"12345{first_name}"
            user = Teacher.objects.create(username=username, first_name=first_name, last_name=last_name, phone=phone, password=password)
            user.set_password(password)
            user.save()
            return redirect('admin_page')
    else:
        form = AddTeacherForm()
    return render(request, 'add_student.html', {'form': form})


def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = AddCourseForm()
    return render(request, 'add_student.html', {'form': form})


def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = AddGroupForm()  # Re-render form with errors if not valid
    return render(request, 'add_student.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_page')
        # else:
        #     messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def teachers_view(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers.html', context)


def edit_teacher_view(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = EditTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    form = EditTeacherForm(instance=teacher)
    return render(request, 'edit_teacher.html', {'form': form})