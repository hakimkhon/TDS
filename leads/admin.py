from django.contrib import admin

from .models import Lead, User, Agent, UserProfil
admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(UserProfil)
