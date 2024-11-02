from django import forms

from users.models import Student, Teacher, Course, Group


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone', 'group']


class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'phone']

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'teacher', 'course', 'day', 'start_date', 'end_date', 'lesson_time']


class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'phone', 'username']