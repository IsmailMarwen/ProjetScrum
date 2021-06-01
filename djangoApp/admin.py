from django.contrib import admin
from .models import *
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'team')
    search_fields = ('name',)
    list_filter = ('team',)
class ProjectInline(admin.TabularInline):
    model = Project
class TeamAdmin(admin.ModelAdmin):
    inlines = (ProjectInline,)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(ProductBacklog)
admin.site.register(Sprint)
admin.site.register(UserStory)
