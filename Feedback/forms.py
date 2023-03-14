from django import forms

from Review.models import Semester
from .models import FeedbackData

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackData
        exclude = ['total', 'average']
        labels = {
            'teacher_name': 'Name of Teacher',
            'semester': 'Semester',
            'punctuality': 'The teacher is punctual in coming to class',
            'portion': 'The teacher completes portions at the appropriate time',
            'doubt': 'The teacher takes in effort to clear your doubts',
            'interactive': 'The teacher makes the class interactive',
            'comments': 'Any other feedback (your comments)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically generate semester choices based on selected teacher_name
        self.fields['semester'].queryset = self.fields['semester'].queryset.none()

        if 'teacher_name' in self.data:
            try:
                teacher_id = int(self.data.get('teacher_name'))
                self.fields['semester'].queryset = Semester.objects.filter(faculty_id=teacher_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Semester queryset
        elif self.instance.pk:
            self.fields['semester'].queryset = self.instance.teacher_name.semesters.all()
