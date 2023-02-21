from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from Feedback.models import FeedbackData
from .forms import UserForm

class ListFeedbackView(LoginRequiredMixin, ListView):
    model = FeedbackData
    template_name = 'Review/list_feedback.html'
    context_object_name = 'feedbacks'
    ordering = ['-date_submitted']
    paginate_by = 10

def loginPage(request):
    context = {}
    return render(request,'Review/student_login.html',context)

def registerPage(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form' : form}
    return render(request,'Review/register.html',context)

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