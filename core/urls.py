
from django.contrib import admin
from django.urls import path, include
from leads.views import Galereya, HomePage, SignupView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view()),
    path('leads/', include('leads.urls', namespace = "leads")),
    path('agents/', include('agents.urls', namespace = "agents")),
    path('login/', LoginView.as_view(), name = "login"),
    path('signup/', SignupView.as_view(), name = "signup"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('galery/', Galereya.as_view(), name="galery"),
]
