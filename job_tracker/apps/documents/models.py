from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.jobs.models import Application


class GeneratedDocument(models.Model):
    """Generated CV and cover letter documents"""
    DOCUMENT_TYPES = [
        ('cv', 'CV/Resume'),
        ('cover_letter', 'Cover Letter'),
        ('email_response', 'Email Response'),
        ('follow_up', 'Follow-up Email'),
    ]
    
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    content = models.TextField()
    language = models.CharField(max_length=5)
    google_docs_id = models.CharField(max_length=100, blank=True)
    google_docs_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Generated Document")
        verbose_name_plural = _("Generated Documents")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_document_type_display()} for {self.application.job.title}"


class DocumentVersion(models.Model):
    """Version control for generated documents"""
    document = models.ForeignKey(GeneratedDocument, on_delete=models.CASCADE, related_name='versions')
    version_number = models.IntegerField()
    content = models.TextField()
    changes_summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Document Version")
        verbose_name_plural = _("Document Versions")
        ordering = ['-version_number']
        unique_together = ['document', 'version_number']

    def __str__(self):
        return f"Version {self.version_number} of {self.document}"


class AIGenerationLog(models.Model):
    """Log of AI content generation requests"""
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='ai_logs')
    document_type = models.CharField(max_length=20, choices=GeneratedDocument.DOCUMENT_TYPES)
    prompt_used = models.TextField()
    response_received = models.TextField()
    tokens_used = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    language = models.CharField(max_length=5)
    success = models.BooleanField(default=True)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("AI Generation Log")
        verbose_name_plural = _("AI Generation Logs")
        ordering = ['-created_at']

    def __str__(self):
        return f"AI Generation for {self.application.job.title} - {self.document_type}"
