from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User,Faculty,Subject,Semester
from .models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('name','gmail','password','student_id')

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        widgets = {
            'subject': forms.CheckboxSelectMultiple(),
        }
        fields = ['name', 'gmail', 'password', 'semester', 'subject', 'batch']

    def __init__(self, *args, **kwargs):
        super(FacultyForm, self).__init__(*args, **kwargs)
        self.fields['semester'].queryset = Semester.objects.all()
        self.fields['subject'].queryset = Subject.objects.none()

        if 'semester' in self.data:
            try:
                semester_id = int(self.data.get('semester'))
                self.fields['subject'].queryset = Subject.objects.filter(semester_id=semester_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.semester.subject_set.order_by('name')

        
class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('gmail','password')