from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('feedback/', include('Feedback.urls')),
    path('review/', include('Review.urls')),
    path('login/',
         auth_views.LoginView.as_view(template_name='Review/login.html'),
         name='LoginView'),
    path('studentlogin/',
         auth_views.LoginView.as_view(template_name='Review/student_login.html'),
         name='StudentLoginView'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='Review/logout.html'),
         name='LogoutView'),
]