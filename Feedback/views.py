from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect, JsonResponse
from Review.models import Semester, Faculty
from .models import FeedbackData


class GetFeedbackView(CreateView):
    model = FeedbackData
    fields = [ 'teacher_name', 'semester', 'punctuality', 'portion', 'doubt', 'interactive', 'comments']
    template_name = 'Feedback/feedback_form.html'

class SuccessView(TemplateView):
    template_name = 'Feedback/success.html'


def get_semesters_for_faculty(req,facultyId):
    print(facultyId)
    # Get the faculty
    faculty = Faculty.objects.get(id=facultyId)
    print(faculty)
    # Get the semesters for the faculty
    semesters = faculty.semester.all()

    for semester in semesters:
        print(semester.name)

    # Serialize the semesters as JSON
    data = [{'id': semester.id, 'name': semester.name} for semester in semesters]

    return JsonResponse(data, safe=False)


# class importExcel(CreateView):
    
#     def get(self,request):
#         feedback_obj = FeedbackData.objects.all()
#         # serializer = FeedbackSerializer(feedback_obj,many = True)
#         df = pd.DataFrame(feedback_obj)
#         print(df)

#         return HttpResponseRedirect('HomeView')

