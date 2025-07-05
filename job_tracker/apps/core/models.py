from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class JobPlatform(models.Model):
    """Job platform configuration for API integrations"""
    name = models.CharField(max_length=50)  # linkedin, xing, stepstone, etc.
    api_endpoint = models.URLField()
    api_key = models.CharField(max_length=255)
    rate_limit = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Job Platform")
        verbose_name_plural = _("Job Platforms")
        ordering = ['name']

    def __str__(self):
        return self.name


class TranslationCache(models.Model):
    """Cache translations to avoid repeated API calls"""
    source_text_hash = models.CharField(max_length=64, db_index=True)  # SHA256 hash
    source_language = models.CharField(max_length=5)
    target_language = models.CharField(max_length=5)
    translated_text = models.TextField()
    translation_service = models.CharField(max_length=50)  # libretranslate, google, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['source_text_hash', 'source_language', 'target_language']
        indexes = [
            models.Index(fields=['source_text_hash', 'source_language', 'target_language']),
        ]
        verbose_name = _("Translation Cache")
        verbose_name_plural = _("Translation Cache")

    def __str__(self):
        return f"{self.source_language} -> {self.target_language} ({self.translation_service})"


class DocumentTemplate(models.Model):
    """Multi-language document templates"""
    TEMPLATE_TYPES = [
        ('cv', 'CV/Resume'),
        ('cover_letter', 'Cover Letter'),
        ('email_response', 'Email Response'),
        ('follow_up', 'Follow-up Email'),
    ]

    name = models.CharField(max_length=100)
    template_type = models.CharField(max_length=20, choices=TEMPLATE_TYPES)
    language = models.CharField(max_length=5)
    content = models.TextField()
    variables = models.JSONField(default=dict)  # Template variables like {name}, {company}
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Document Template")
        verbose_name_plural = _("Document Templates")
        ordering = ['template_type', 'language', 'name']

    def __str__(self):
        return f"{self.get_template_type_display()} - {self.name} ({self.language})"


class MarketInsight(models.Model):
    """Market analytics and insights"""
    platform = models.ForeignKey(JobPlatform, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    demand_score = models.FloatField()  # Job demand for this skill
    avg_salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    date_analyzed = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Market Insight")
        verbose_name_plural = _("Market Insights")
        ordering = ['-date_analyzed', 'platform', 'skill']

    def __str__(self):
        return f"{self.skill} - {self.platform.name} ({self.location})"


class TranslationUsage(models.Model):
    """Track translation usage and costs"""
    service_name = models.CharField(max_length=50)
    character_count = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = _("Translation Usage")
        verbose_name_plural = _("Translation Usage")
        ordering = ['-date', 'service_name']

    def __str__(self):
        return f"{self.service_name} - {self.character_count} chars ({self.date})"

    @classmethod
    def log_usage(cls, service, text, cost=0):
        return cls.objects.create(
            service_name=service,
            character_count=len(text),
            cost=cost
        )
