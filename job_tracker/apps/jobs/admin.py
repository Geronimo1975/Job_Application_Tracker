from django.contrib import admin
from .models import Job, Application, JobSearchCriteria


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'platform', 'posted_date', 'detected_language']
    list_filter = ['platform', 'posted_date', 'detected_language', 'company_rating']
    search_fields = ['title', 'company', 'description']
    readonly_fields = ['scraped_date']
    date_hierarchy = 'posted_date'


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'status', 'applied_date', 'target_language', 'created_at']
    list_filter = ['status', 'target_language', 'created_at', 'applied_date']
    search_fields = ['job__title', 'job__company', 'notes']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'


@admin.register(JobSearchCriteria)
class JobSearchCriteriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'keywords', 'location', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'keywords', 'location']
    filter_horizontal = ['platforms']
    readonly_fields = ['created_at', 'updated_at']
