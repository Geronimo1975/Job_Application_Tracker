from django.db import models
from django.utils.translation import gettext_lazy as _


class DashboardWidget(models.Model):
    """Dashboard widget configuration"""
    WIDGET_TYPES = [
        ('stats', 'Statistics'),
        ('chart', 'Chart'),
        ('list', 'List'),
        ('calendar', 'Calendar'),
    ]
    
    name = models.CharField(max_length=100)
    widget_type = models.CharField(max_length=20, choices=WIDGET_TYPES)
    configuration = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Dashboard Widget")
        verbose_name_plural = _("Dashboard Widgets")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class UserPreference(models.Model):
    """User preferences for dashboard and application"""
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('de', 'German'),
        ('auto', 'Auto-detect'),
    ]
    
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    preferred_language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='auto')
    dashboard_layout = models.JSONField(default=dict)
    email_notifications = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Preference")
        verbose_name_plural = _("User Preferences")

    def __str__(self):
        return f"Preferences for {self.user.username}"


class AnalyticsEvent(models.Model):
    """Track user interactions and analytics events"""
    EVENT_TYPES = [
        ('job_view', 'Job View'),
        ('application_create', 'Application Created'),
        ('document_generate', 'Document Generated'),
        ('email_sent', 'Email Sent'),
        ('translation_used', 'Translation Used'),
    ]
    
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    data = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Analytics Event")
        verbose_name_plural = _("Analytics Events")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_event_type_display()} - {self.created_at}"
