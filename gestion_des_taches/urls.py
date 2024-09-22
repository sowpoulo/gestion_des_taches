from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
# Fonction pour rediriger la racine vers la liste des tâches
def home_redirect(request):
    return redirect('task_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect),  # Redirige la racine vers la liste des tâches
    path('tasks/', include('tasks.urls')),  # Inclut les URLs de l'application tasks
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Vue pour le login
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),  # Vue pour le logout
]
