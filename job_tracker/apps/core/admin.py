from django.contrib import admin
from .models import JobPlatform, TranslationCache, DocumentTemplate, MarketInsight, TranslationUsage


@admin.register(JobPlatform)
class JobPlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_endpoint', 'rate_limit', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'api_endpoint']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(TranslationCache)
class TranslationCacheAdmin(admin.ModelAdmin):
    list_display = ['source_language', 'target_language', 'translation_service', 'created_at']
    list_filter = ['source_language', 'target_language', 'translation_service', 'created_at']
    search_fields = ['source_text_hash', 'translated_text']
    readonly_fields = ['created_at']


@admin.register(DocumentTemplate)
class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'template_type', 'language', 'is_active', 'created_at']
    list_filter = ['template_type', 'language', 'is_active', 'created_at']
    search_fields = ['name', 'content']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(MarketInsight)
class MarketInsightAdmin(admin.ModelAdmin):
    list_display = ['skill', 'platform', 'demand_score', 'avg_salary', 'location', 'date_analyzed']
    list_filter = ['platform', 'location', 'date_analyzed']
    search_fields = ['skill', 'location']
    readonly_fields = ['date_analyzed']


@admin.register(TranslationUsage)
class TranslationUsageAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'character_count', 'cost', 'date']
    list_filter = ['service_name', 'date']
    readonly_fields = ['date']
