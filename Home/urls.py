from django.urls import path
from django.contrib import admin
from .views import HomeView, AboutUs , ContactUs, get_teachers

admin.site.site_header = "Student Feedback Review"
admin.site.site_title = "Welcome to Our website"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('aboutus/', AboutUs.as_view(), name='AboutUs'),
    path('contactus/', ContactUs.as_view(), name='ContactUs'),
    path('ajax_calls/autocomplete_search_func', get_teachers, name='get_teachers'),
]