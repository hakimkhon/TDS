
from django.contrib import admin
from django.urls import path, include
from leads.views import Galereya, HomePage, SignupView
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view()),
    path('leads/', include('leads.urls', namespace = "leads")),
    path('agents/', include('agents.urls', namespace = "agents")),
    path('login/', LoginView.as_view(), name = "login"),
    path('password_reset/', PasswordResetView.as_view(), name = "password_reset"),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name = "password_reset_complete"),
    path('signup/', SignupView.as_view(), name = "signup"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('galery/', Galereya.as_view(), name="galery"),
]
