from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead_lists"),
    path('yaratish/', LeadCreateView.as_view(), name="lead_create"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead_details"),
    path('<int:pk>/uchirish/', LeadDeleteView.as_view(), name="lead_delete"),
    path('<int:pk>/uzgartirish/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/agentni_aniqla', AgentAssaginView.as_view(), name="agentni_aniqla"),
    
]
