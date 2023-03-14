from django.urls import path
from .views import  GetFeedbackView, SuccessView, get_semesters_for_faculty

urlpatterns = [
    path('', GetFeedbackView.as_view(), name='GetFeedbackView'),
    path('success/', SuccessView.as_view(), name='SuccessView'),

    path('api/semesters/<int:facultyId>/', get_semesters_for_faculty),
    # path('excel/', importExcel.as_view(), name = 'importExcel'),
]