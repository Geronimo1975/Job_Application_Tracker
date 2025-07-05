from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.jobs.models import Application


class EmailAccount(models.Model):
    """Email account configuration"""
    email = models.EmailField()
    imap_server = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  # Encrypted
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Email Account")
        verbose_name_plural = _("Email Accounts")
        ordering = ['email']

    def __str__(self):
        return self.email


class EmailThread(models.Model):
    """Email conversation thread"""
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='email_threads')
    thread_id = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    participants = models.JSONField()  # List of email addresses
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Email Thread")
        verbose_name_plural = _("Email Threads")
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.subject} - {self.application.job.company}"


class Email(models.Model):
    """Individual email message"""
    EMAIL_TYPES = [
        ('inbound', 'Received'),
        ('outbound_manual', 'Sent Manually'),
        ('outbound_auto', 'Sent Automatically'),
    ]
    
    thread = models.ForeignKey(EmailThread, on_delete=models.CASCADE, related_name='emails')
    message_id = models.CharField(max_length=255, unique=True)
    sender = models.EmailField()
    recipients = models.JSONField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    email_type = models.CharField(max_length=20, choices=EMAIL_TYPES)
    sent_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.subject} from {self.sender}"


class GoogleIntegration(models.Model):
    """Google Workspace integration configuration"""
    INTEGRATION_TYPES = [
        ('sheets', 'Google Sheets'),
        ('docs', 'Google Docs'),
        ('gmail', 'Gmail'),
    ]
    
    integration_type = models.CharField(max_length=20, choices=INTEGRATION_TYPES)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    access_token = models.TextField(blank=True)
    refresh_token = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Google Integration")
        verbose_name_plural = _("Google Integrations")
        ordering = ['integration_type']

    def __str__(self):
        return f"{self.get_integration_type_display()} Integration"


class APIConfiguration(models.Model):
    """API configuration for external services"""
    SERVICE_TYPES = [
        ('linkedin', 'LinkedIn'),
        ('xing', 'Xing'),
        ('stepstone', 'StepStone'),
        ('indeed', 'Indeed'),
        ('glassdoor', 'Glassdoor'),
        ('openai', 'OpenAI'),
    ]
    
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255, blank=True)
    base_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("API Configuration")
        verbose_name_plural = _("API Configurations")
        ordering = ['service_type']

    def __str__(self):
        return f"{self.get_service_type_display()} API Configuration"
