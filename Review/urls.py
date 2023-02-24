from . import views
from django.urls import path
from .views import ListFeedbackView, SearchResultsView, deleteAllFeedback, FeedbackDetailView, DeleteFeedbackView, facultyRegister, load_subjects,loginPage,registerPage,FacultyView

urlpatterns = [
    path('', ListFeedbackView.as_view(), name='ListFeedbackView'),
    path('search/', SearchResultsView.as_view(), name='SearchResultsView'),
    path('student_login', loginPage, name='LoginPage'),
    path('register', registerPage, name='RegisterPage'),
    path('faculty_login', FacultyView, name='FacultyView'),
    path('review/detail_feedback', FeedbackDetailView.as_view(), name='FeedbackDetailView'),
    path('facultyregister', facultyRegister, name='FacultyRegisterPage'),
    path('delete/', deleteAllFeedback, name='deleteAllFeedback'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='FeedbackDetailView'),
    path('feedback/<int:pk>/delete/', DeleteFeedbackView.as_view(), name='DeleteFeedbackView'),
    
    path('<int:pk>/', views.faculty_update_view, name='faculty_change'),
    path('ajax/load-subjects/', views.load_subjects, name='ajax_load_subjects')
]