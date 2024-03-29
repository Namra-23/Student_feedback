from Review.views import export_to_excel
from . import views
from django.urls import path
from .views import   Allchart, ListFeedbackView, SearchResultsView, deleteAllFeedback, FeedbackDetailView,FacultyFeedbackDetailView, DeleteFeedbackView, facultyRegister, load_subjects,loginPage,registerPage,FacultyView,FacultyFeedbackList,FacultyFeedback,Chart

urlpatterns = [
    path('', ListFeedbackView.as_view(), name='ListFeedbackView'),
    path('search/', SearchResultsView.as_view(), name='SearchResultsView'),
    path('student_login', loginPage, name='LoginPage'),
    path('register', registerPage, name='RegisterPage'),
    path('faculty_login', FacultyView, name='FacultyView'),
    path('faculty_feedback', FacultyFeedbackList.as_view(), name='FacultyFeedbackList'),
    path('review/detail_feedback', FeedbackDetailView.as_view(), name='FeedbackDetailView'),
    path('facultyregister', facultyRegister, name='FacultyRegisterPage'),
    path('delete/', deleteAllFeedback, name='deleteAllFeedback'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='FeedbackDetailView'),
    path('faculty_feedback/<int:pk>/', FacultyFeedback.as_view(), name='FacultyFeedback'),
    path('faculty_detail_feedback/<int:pk>/', FacultyFeedbackDetailView.as_view(), name='FacultyFeedbackDetailView'),
    path('feedback/<int:pk>/delete/', DeleteFeedbackView.as_view(), name='DeleteFeedbackView'),
    
    path('<int:pk>/', views.faculty_update_view, name='faculty_change'),
    path('ajax/load-subjects/', views.load_subjects, name='ajax_load_subjects'),
    # for chart
    path('chart/', Chart, name='Chart'),
    path('allchart/', Allchart, name='AllChart'),
    path('export-to-excel/', export_to_excel, name='export-to-excel'),
]