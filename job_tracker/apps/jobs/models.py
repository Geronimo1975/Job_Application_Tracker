from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import JobPlatform


class Job(models.Model):
    """Job posting model"""
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    requirements = models.TextField()
    url = models.URLField(unique=True)
    platform = models.ForeignKey(JobPlatform, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=100)  # Platform-specific ID
    posted_date = models.DateTimeField()
    scraped_date = models.DateTimeField(auto_now_add=True)
    company_rating = models.FloatField(null=True, blank=True)  # From Glassdoor
    company_size = models.CharField(max_length=50, blank=True)
    detected_language = models.CharField(max_length=5, default='en')
    description_translated = models.TextField(blank=True)
    translation_language = models.CharField(max_length=5, blank=True)

    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")
        ordering = ['-posted_date']
        indexes = [
            models.Index(fields=['title', 'company']),
            models.Index(fields=['platform', 'posted_date']),
            models.Index(fields=['detected_language']),
        ]

    def __str__(self):
        return f"{self.title} at {self.company}"


class Application(models.Model):
    """Job application tracking"""
    STATUS_CHOICES = [
        ('not_applied', 'Not Applied'),
        ('applied', 'Applied'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('interviewed', 'Interviewed'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]

    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('de', 'German'),
        ('auto', 'Auto-detect'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_applied')
    applied_date = models.DateTimeField(null=True, blank=True)
    target_language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='auto')
    cv_version = models.TextField(blank=True)  # Generated CV content
    cv_original_language = models.CharField(max_length=5, default='en')
    cover_letter = models.TextField(blank=True)  # Generated cover letter
    cover_letter_original_language = models.CharField(max_length=5, default='en')
    google_docs_cv_id = models.CharField(max_length=100, blank=True)
    google_docs_cl_id = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")
        ordering = ['-created_at']

    def __str__(self):
        return f"Application for {self.job.title} at {self.job.company}"


class JobSearchCriteria(models.Model):
    """Search criteria for job scraping"""
    name = models.CharField(max_length=100)
    keywords = models.TextField(help_text="Comma-separated keywords")
    location = models.CharField(max_length=100, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    platforms = models.ManyToManyField(JobPlatform)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Job Search Criteria")
        verbose_name_plural = _("Job Search Criteria")
        ordering = ['name']

    def __str__(self):
        return self.name
