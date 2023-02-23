from django.urls import path
from .views import ListFeedbackView, SearchResultsView, deleteAllFeedback, FeedbackDetailView, DeleteFeedbackView,loginPage,registerPage

urlpatterns = [
    path('', ListFeedbackView.as_view(), name='ListFeedbackView'),
    path('search/', SearchResultsView.as_view(), name='SearchResultsView'),
    path('student_login', loginPage, name='LoginPage'),
    path('register', registerPage, name='RegisterPage'),
    path('review/detail_feedback', FeedbackDetailView.as_view(), name='FeedbackDetailView'),
    path('delete/', deleteAllFeedback, name='deleteAllFeedback'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='FeedbackDetailView'),
    path('feedback/<int:pk>/delete/', DeleteFeedbackView.as_view(), name='DeleteFeedbackView')
]