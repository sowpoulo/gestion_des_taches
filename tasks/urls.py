from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
    # URL pour les pages de login, register, etc.
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('password/', views.password_reset_view, name='password_reset'),
    path('tables/', views.tables_view, name='tables'),
]
