# from audioop import reverse
from ast import Assign
from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import redirect, render, reverse
from agents.mixins import OrganiserAndLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models 
from .forms import *
from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
    FormView
)

# class HomePage(TemplateView):
#     template_name = ("home.html")

class Galereya(ListView):
    template_name = ("lead\galereya.html")
    queryset = models.Lead.objects.all()
    # context_object_name = "lead"

class HomePage(ListView):
    template_name = ("home.html")
    queryset = models.Lead.objects.all()
    context_object_name = "all"

class SignupView(CreateView):
    template_name = ("registration/signup.html")
    form_class = NewUserForm

    def get_success_url(self):
        return reverse('leads:lead_lists')

class LeadListView(LoginRequiredMixin, ListView):
    template_name = ("lead/lead_lists.html")
    # queryset = models.Lead.objects.all()
    context_object_name = "leads"
    
    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            queryset = Lead.objects.filter(organisation = user.userprofil)
        else: 
            queryset = Lead.objects.filter(organisation = user.agent.organisation)
            queryset = queryset.filter(agent__user = self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_admin:
            queryset = Lead.objects.filter(
                organisation = user.userprofil,
                agent__isnull = True
            )
            context.update({
                "unassigned_leads": queryset
            })
        return context
class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = ("lead/lead_details.html")
    queryset = models.Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = ("lead/lead_create.html")
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_lists')

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = ("lead/lead_update.html")
    form_class = LeadModelForm
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_lists')

class LeadDeleteView(OrganiserAndLoginRequiredMixin, DeleteView):
    template_name = ("lead/lead_delete.html")
    form_class = LeadModelForm
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_lists')

class AgentAssaginView(OrganiserAndLoginRequiredMixin, FormView):
    template_name = ("lead/agentni_aniqlash.html")
    form_class = AssignAgentForm
    queryset = models.Lead.objects.all()

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AgentAssaginView, self).get_form_kwargs( **kwargs)
        kwargs.update({
                "request": self.request
            })
        return kwargs
    def get_success_url(self):
        return reverse('leads:lead_lists')

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id = self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AgentAssaginView, self).form_valid(form)
