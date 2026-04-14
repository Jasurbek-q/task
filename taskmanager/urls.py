from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.task_list, name='task_list'),
    path('register/', task_views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tasks/create/', task_views.task_create, name='task_create'),
    path('tasks/<int:pk>/', task_views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', task_views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', task_views.task_delete, name='task_delete'),
]
