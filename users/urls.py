from django.urls import path, include

from . import views

app_name = "users"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/profile', views.ProfileUpdateView.as_view(), name='profile')
]