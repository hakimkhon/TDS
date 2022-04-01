from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead_lists"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead_details"),
    path('<int:pk>/uzgartirish/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/uchirish/', LeadDeleteView.as_view(), name="lead_delete"),
    path('yaratish/', LeadCreateView.as_view(), name="lead_create"),
    
]
