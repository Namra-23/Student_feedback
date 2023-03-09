from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from Feedback.models import FeedbackData
from .forms import UserForm,FacultyForm
from .models import Faculty, Subject,Semester
from Feedback.views import GetFeedbackView
from .forms import UserForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .models import User,Faculty
from django.views.generic import TemplateView

# For all Faculties
class ListFeedbackView(LoginRequiredMixin, ListView):
    model = FeedbackData
    template_name = 'Review/list_feedback.html'
    context_object_name = 'feedbacks'
    ordering = ['-date_submitted']
    paginate_by = 10

# For particular Faculty
class FacultyFeedbackList(ListView):
    
    model = FeedbackData
    template_name = 'Review/faculty_feedback.html'
    context_object_name = 'feedbacks'
    ordering = ['-date_submitted']
    paginate_by = 10
    email = None
    def get_queryset(self):
        # email = self.request.POST.get('gmail')
        # print(request.method)
        print("helloooooooooooooo ",FacultyFeedbackList.email)
        user = Faculty.GetUserByEmail(FacultyFeedbackList.email)
        object_list = FeedbackData.objects.filter(teacher_name__name__icontains=user.name)
        object_list = object_list.order_by('-date_submitted')
        return object_list
    @staticmethod
    def setEmail(email):
        print("hi",email)
        FacultyFeedbackList.email=email

# For Faculty login
def FacultyView(request):
    # template_name = 'Review/faculty_login.html'
    if request.method == 'POST':
        email = request.POST.get('gmail')
        print(email)
        FacultyFeedbackList().setEmail(email)
        password = request.POST.get('password')
        login_form = LoginForm()
        user = Faculty.GetUserByEmail(email)
        if user is not None:
            if user.password == password:
                return redirect('FacultyFeedbackList')
                # return render(request, 'Review/faculty_feedback.html')
        else:
            messages.info(request, 'Username or password is incorrect')
    context={}
    return render(request, 'Review/faculty_login.html',context)

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('gmail')
        password = request.POST.get('password')
        login_form = LoginForm()
        user = User.GetUserByEmail(email)
        if user is not None:
            if user.password == password:
                return redirect('GetFeedbackView')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request,'Review/student_login.html',context)

def registerPage(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('name')
            # messages.success(request, "Account is created for " + user)
            
            return redirect('LoginPage')
    
    context = {'form' : form}
    return render(request,'Review/register.html',context)


def facultyRegister(request):
    form = FacultyForm()

    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form' : form}
    return render(request,'Review/faculty_registration.html',context)

def faculty_update_view(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    form = FacultyForm(instance=faculty)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_change', pk=pk)
    context = {'form' : form}
    return render(request,'Review/faculty_registration.html',context)

def load_subjects(request):
    sem_id = request.GET.get('sem_id')
    subjects = Subject.objects.filter(semester_id=sem_id)
    return render(request, 'Review/subject_dropdown_list_options.html', {'subjects': subjects})
    # return JsonResponse(list(subjects.values('id', 'name')), safe=False)

class SearchResultsView(LoginRequiredMixin, ListView):
    model = FeedbackData
    template_name = 'Review/list_feedback.html'
    context_object_name = 'feedbacks'
    ordering = ['-date_submitted']
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = FeedbackData.objects.filter(teacher_name__name__icontains=query)
        object_list = object_list.order_by('-date_submitted')
        return object_list


class FeedbackDetailView(LoginRequiredMixin, DetailView):
    model = FeedbackData
    template_name = 'Review/detail_feedback.html'
    context_object_name = 'feedback'


class DeleteFeedbackView(LoginRequiredMixin, DeleteView):
    model = FeedbackData
    context_object_name = 'feedback'
    template_name = 'Review/confirm_delete.html'
    success_url = '/review/'


@login_required
def deleteAllFeedback(request):
    FeedbackData.objects.all().delete()
    context = {}

    return render(request, 'Review/delete_success_feedback.html', context)