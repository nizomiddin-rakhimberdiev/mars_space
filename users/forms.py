from django import forms

from users.models import Student


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone', 'group']