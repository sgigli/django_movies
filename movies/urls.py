from django.urls import path

from . import views

app_name = "movies"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create', views.CreateView.as_view(), name='create'),
    path('<int:pk>/edit', views.UpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name="delete")
]