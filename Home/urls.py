from django.urls import path
from .views import HomeView, AboutUs , ContactUs, get_teachers

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('aboutus/', AboutUs.as_view(), name='AboutUs'),
    path('contactus/', ContactUs.as_view(), name='ContactUs'),
    path('ajax_calls/autocomplete_search_func', get_teachers, name='get_teachers'),
]