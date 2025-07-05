# Django Job Application Tracker - Cursor Development Prompt

## Project Overview
Create a Django web application for job application tracking with automated job scraping, AI-powered CV/cover letter personalization, and Google Workspace integration. The application should support both German and English languages.

## Core Features Required

### 1. Job Scraping & Monitoring
- **Job Board Integration**: Scrape jobs from major German job boards (StepStone, Xing, Indeed.de, LinkedIn)
- **Keyword Filtering**: Filter jobs based on skills, location, salary range, and company preferences
- **Automated Monitoring**: Schedule periodic scraping with Celery/Redis
- **Duplicate Detection**: Prevent duplicate job entries using URL/title matching
- **Job Status Tracking**: Track application status (Not Applied, Applied, Interview, Rejected, Accepted)

### 2. AI-Powered Document Generation
- **OpenAI Integration**: Use GPT-4 for CV and cover letter personalization
- **Template Management**: Store base CV/cover letter templates
- **Job-Specific Customization**: Tailor documents based on job requirements
- **Multi-language Support**: Generate documents in German and English
- **Content Optimization**: Match keywords from job descriptions

### 3. Google Workspace Integration
- **Google Sheets API**:
  - Export job applications data
  - Sync application status updates
  - Generate reports and analytics
- **Google Docs API**:
  - Store generated CVs and cover letters
  - Create shareable document links
  - Version control for document iterations

### 4. Job Board API Integration & Analytics
- **LinkedIn Jobs API**: Official LinkedIn talent solutions integration
- **Xing API**: Access to German professional network job postings
- **StepStone API**: Integration with StepStone's job search API
- **Indeed API**: Publisher and job search API integration
- **Glassdoor API**: Company reviews, salary data, and job listings
- **Data Pipeline**: Real-time job data synchronization and processing
- **Market Analytics**:
  - Salary trend analysis across platforms
  - Company reputation scoring (Glassdoor integration)
  - Job market insights and demand forecasting
  - Skill gap analysis based on job requirements

### 5. Email Integration & Automation
- **IMAP/SMTP Integration**: Connect to email accounts (Gmail, Outlook, corporate)
- **Email Parsing**: Extract job-related emails and responses
- **Automated Responses**: AI-powered personalized email replies
- **Email Templates**: Smart templates for follow-ups, thank you notes, interview confirmations
- **Email Tracking**: Monitor email open rates and response times
- **Calendar Integration**: Automatic interview scheduling from emails

### 6. AI-Powered Communication
- **Response Generation**: Create personalized responses to recruiter emails
- **Follow-up Automation**: Smart follow-up emails based on application timeline
- **Interview Preparation**: Generate interview questions and answers based on job requirements
- **Rejection Analysis**: Learn from rejection emails to improve applications
- **Sentiment Analysis**: Analyze recruiter communication tone and adjust responses

### 7. Web Interface
- **Dashboard**: Overview of applications, success rates, and upcoming deadlines
- **Job Management**: Add, edit, and track job applications
- **Document Preview**: View and edit generated documents
- **Analytics Dashboard**:
  - Cross-platform job market analysis
  - Application success rates by platform
  - Salary benchmarking
  - Company insights and ratings
- **Email Management**: Unified inbox for job-related communications
- **AI Response Center**: Review and approve automated email responses

## Technical Requirements

### Django Architecture
```python
# Project Structure
job_tracker/
├── apps/
│   ├── core/           # Base models and utilities
│   ├── jobs/           # Job models and scraping logic
│   ├── documents/      # CV/Cover letter generation
│   ├── integrations/   # Google APIs and OpenAI
│   └── dashboard/      # Main UI and analytics
├── static/
├── templates/
├── requirements.txt
└── docker-compose.yml
```

### API Integration Requirements
```python
# Required APIs and SDKs
REQUIRED_APIS = {
    'linkedin': 'LinkedIn Jobs API & Talent Solutions',
    'xing': 'XING API for German market',
    'stepstone': 'StepStone Partner API',
    'indeed': 'Indeed Publisher & Job Search API',
    'glassdoor': 'Glassdoor API for company data',
    'openai': 'GPT-4 for content generation',
    'google_sheets': 'Google Sheets API v4',
    'google_docs': 'Google Docs API v1',
    'gmail': 'Gmail API for email integration'
}
```

### Key Models
```python
# jobs/models.py
class JobPlatform(models.Model):
    name = models.CharField(max_length=50)  # linkedin, xing, stepstone, etc.
    api_endpoint = models.URLField()
    api_key = models.CharField(max_length=255)
    rate_limit = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField()
    requirements = models.TextField()
    url = models.URLField(unique=True)
    platform = models.ForeignKey(JobPlatform, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=100)  # Platform-specific ID
    posted_date = models.DateTimeField()
    scraped_date = models.DateTimeField(auto_now_add=True)
    company_rating = models.FloatField(null=True)  # From Glassdoor
    company_size = models.CharField(max_length=50, blank=True)

class Application(models.Model):
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

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    applied_date = models.DateTimeField(null=True)
    target_language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='auto')
    cv_version = models.TextField()  # Generated CV content
    cv_original_language = models.CharField(max_length=5, default='en')
    cover_letter = models.TextField()  # Generated cover letter
    cover_letter_original_language = models.CharField(max_length=5, default='en')
    google_docs_cv_id = models.CharField(max_length=100, blank=True)
    google_docs_cl_id = models.CharField(max_length=100, blank=True)

# translations/models.py
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

# communications/models.py
class EmailAccount(models.Model):
    email = models.EmailField()
    imap_server = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  # Encrypted
    is_active = models.BooleanField(default=True)

class EmailThread(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    thread_id = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    participants = models.JSONField()  # List of email addresses

class Email(models.Model):
    EMAIL_TYPES = [
        ('inbound', 'Received'),
        ('outbound_manual', 'Sent Manually'),
        ('outbound_auto', 'Sent Automatically'),
    ]
    thread = models.ForeignKey(EmailThread, on_delete=models.CASCADE)
    message_id = models.CharField(max_length=255, unique=True)
    sender = models.EmailField()
    recipients = models.JSONField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    email_type = models.CharField(max_length=20, choices=EMAIL_TYPES)

# Analytics Models
class MarketInsight(models.Model):
    platform = models.ForeignKey(JobPlatform, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    demand_score = models.FloatField()  # Job demand for this skill
    avg_salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    date_analyzed = models.DateTimeField(auto_now_add=True)
```

### Core Services Implementation

#### 1. Job Scraping Service
```python
# integrations/services/job_scrapers.py
class JobScrapingService:
    def __init__(self):
        self.platforms = {
            'linkedin': LinkedInJobScraper(),
            'xing': XingJobScraper(),
            'stepstone': StepStoneJobScraper(),
            'indeed': IndeedJobScraper(),
            'glassdoor': GlassdoorJobScraper(),
        }

    async def scrape_all_platforms(self, search_criteria):
        # Parallel scraping with rate limiting
        # API authentication and error handling
        # Data normalization and deduplication

class LinkedInJobScraper:
    def __init__(self):
        self.client = linkedin_api.LinkedInClient()

    async def search_jobs(self, keywords, location, limit=100):
        # LinkedIn Jobs API implementation
        # Handle pagination and rate limits
        # Extract job details and company info
```

#### 2. AI Content Generation & Translation Service
```python
# integrations/services/ai_service.py
class AIContentService:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        self.translation_service = TranslationService()

    def generate_cv(self, job_description, base_cv, target_language='en'):
        # First detect source language
        source_lang = self.translation_service.detect_language(job_description)

        # Translate job description if needed for better AI understanding
        if source_lang != 'en':
            job_desc_en = self.translation_service.translate(job_description, 'en', source_lang)
        else:
            job_desc_en = job_description

        prompt = f"""
        Customize this CV for the following job:
        Job: {job_desc_en}
        Base CV: {base_cv}
        Target Language: {target_language}

        Focus on relevant skills and experience.
        Use professional {target_language} language.
        Adapt cultural expectations for {target_language} job markets.
        """

        response = self.openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        cv_content = response.choices[0].message.content

        # Translate final CV if target language is not English
        if target_language != 'en':
            cv_content = self.translation_service.translate(cv_content, target_language, 'en')

        return cv_content

    def generate_cover_letter(self, job, company_info, target_language='en'):
        # Similar implementation with translation support

    def generate_email_response(self, email_content, context, target_language='en', tone='professional'):
        # Detect email language
        email_lang = self.translation_service.detect_language(email_content)

        # Generate response in detected language or specified target language
        response_lang = target_language if target_language != 'auto' else email_lang

        # AI-powered email response generation with language awareness

    def analyze_job_requirements(self, job_description):
        # Extract skills, requirements, and keywords with multi-language support

# integrations/services/translation_service.py
class TranslationService:
    def __init__(self):
        self.libre_translate_url = settings.LIBRETRANSLATE_URL or "https://libretranslate.de"
        self.backup_services = [
            GoogleTranslateService(),
            ArgosTranslateService(),  # Offline translation
        ]

    def detect_language(self, text):
        """Detect the language of input text"""
        try:
            from langdetect import detect
            return detect(text)
        except:
            # Fallback to LibreTranslate detection
            response = requests.post(f"{self.libre_translate_url}/detect", {
                'q': text
            })
            return response.json()[0]['language']

    def translate(self, text, target_lang, source_lang='auto'):
        """Translate text using LibreTranslate with fallbacks"""
        try:
            # Primary: LibreTranslate (free, privacy-friendly)
            return self._translate_libretranslate(text, target_lang, source_lang)
        except Exception as e:
            logger.warning(f"LibreTranslate failed: {e}")

            # Fallback to other services
            for service in self.backup_services:
                try:
                    return service.translate(text, target_lang, source_lang)
                except:
                    continue

            raise Exception("All translation services failed")

    def _translate_libretranslate(self, text, target_lang, source_lang='auto'):
        """LibreTranslate implementation"""
        payload = {
            'q': text,
            'source': source_lang,
            'target': target_lang,
            'format': 'text'
        }

        response = requests.post(f"{self.libre_translate_url}/translate", data=payload)
        response.raise_for_status()

        return response.json()['translatedText']

    def translate_document_batch(self, documents, target_lang, source_lang='auto'):
        """Batch translate multiple documents efficiently"""
        results = []

        # Split large documents into chunks for better processing
        for doc in documents:
            chunks = self._split_text(doc, max_length=1000)
            translated_chunks = []

            for chunk in chunks:
                translated_chunk = self.translate(chunk, target_lang, source_lang)
                translated_chunks.append(translated_chunk)

            results.append(' '.join(translated_chunks))

        return results

    def _split_text(self, text, max_length=1000):
        """Split text into chunks preserving sentence boundaries"""
        import re
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            if len(current_chunk + sentence) <= max_length:
                current_chunk += sentence + " "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + " "

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

class ArgosTranslateService:
    """Offline translation service using Argos Translate"""
    def __init__(self):
        import argostranslate.package
        import argostranslate.translate

        # Download required language packages
        self._ensure_language_packages()

    def _ensure_language_packages(self):
        """Download required language packages for German-English translation"""
        import argostranslate.package

        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()

        # Install German <-> English packages
        packages_to_install = [
            ('de', 'en'),  # German to English
            ('en', 'de'),  # English to German
        ]

        for from_code, to_code in packages_to_install:
            package = next(
                filter(
                    lambda x: x.from_code == from_code and x.to_code == to_code,
                    available_packages
                ),
                None
            )
            if package and not package.is_installed():
                package.install()

    def translate(self, text, target_lang, source_lang='auto'):
        import argostranslate.translate

        # Detect source language if auto
        if source_lang == 'auto':
            source_lang = self.detect_language(text)

        return argostranslate.translate.translate(text, source_lang, target_lang)

class GoogleTranslateService:
    """Backup translation service using Google Translate"""
    def translate(self, text, target_lang, source_lang='auto'):
        from googletrans import Translator
        translator = Translator()

        result = translator.translate(text, dest=target_lang, src=source_lang)
        return result.text
```

#### 3. Email Integration Service
```python
# integrations/services/email_service.py
class EmailService:
    def __init__(self, email_account):
        self.account = email_account
        self.imap = imaplib.IMAP4_SSL(email_account.imap_server)
        self.smtp = smtplib.SMTP_SSL(email_account.smtp_server)

    def sync_emails(self):
        # Connect to IMAP and fetch job-related emails
        # Parse email content and extract job information
        # Create EmailThread and Email objects

    def send_automated_response(self, email, response_type):
        # Generate AI response based on email content
        # Send email via SMTP
        # Log email in database

    def schedule_follow_up(self, application, days_delay=7):
        # Schedule follow-up emails using Celery
```

#### 4. Google Workspace Integration
```python
# integrations/services/google_service.py
class GoogleSheetsService:
    def __init__(self):
        self.sheets_client = build('sheets', 'v4', credentials=self.get_credentials())

    def export_applications(self, applications):
        # Create/update Google Sheet with application data
        # Include analytics and charts

    def sync_application_status(self):
        # Bi-directional sync with Google Sheets

class GoogleDocsService:
    def __init__(self):
        self.docs_client = build('docs', 'v1', credentials=self.get_credentials())

    def create_cv_document(self, cv_content, application):
        # Create Google Doc from CV content
        # Set sharing permissions
        # Return document ID and shareable link
```

### Background Tasks (Celery)
```python
# tasks.py
@shared_task
def scrape_jobs_task(platform_name, search_criteria):
    # Periodic job scraping

@shared_task
def sync_emails_task(email_account_id):
    # Email synchronization

@shared_task
def generate_market_insights_task():
    # Analyze job market trends

@shared_task
def send_follow_up_email_task(application_id):
    # Automated follow-up emails
```

### API Endpoints
```python
# api/views.py
class JobViewSet(viewsets.ModelViewSet):
    # CRUD operations for jobs
    # Filtering and search capabilities

class ApplicationViewSet(viewsets.ModelViewSet):
    # Application management API

@api_view(['POST'])
def generate_documents(request, application_id):
    # Generate CV and cover letter for specific application

@api_view(['GET'])
def market_analytics(request):
    # Return market insights and trends


### Frontend Implementation (HTMX + Alpine.js)
```html
<!-- templates/dashboard/index.html -->
<div x-data="dashboard()">
    <!-- Real-time job statistics -->
    <div class="stats-grid" hx-get="/api/dashboard-stats/" hx-trigger="every 30s">
        <!-- Auto-refreshing stats -->
    </div>

    <!-- Job search and filtering -->
    <div class="job-filters">
        <input type="text" x-model="search" @input.debounce.500ms="filterJobs()">
        <select x-model="platform" @change="filterJobs()">
            <option value="">All Platforms</option>
            <option value="linkedin">LinkedIn</option>
            <option value="xing">Xing</option>
            <!-- ... -->
        </select>
    </div>

    <!-- AI-powered application assistant -->
    <div class="ai-assistant" x-show="showAssistant">
        <button @click="generateDocuments(job.id)"
                hx-post="/api/generate-documents/"
                hx-indicator="#loading">
            Generate CV & Cover Letter
        </button>
    </div>
</div>
```

### WebSocket Integration
```python
# consumers.py
class JobUpdatesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("job_updates", self.channel_name)
        await self.accept()

    async def job_update(self, event):
        # Send real-time job updates to frontend
        await self.send(text_data=json.dumps(event['data']))
```

## Required Dependencies

### Python Packages
```txt
# Core Django
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
django-environ==0.11.2

# Database
psycopg2-binary==2.9.7
redis==5.0.1

# Async & Background Tasks
celery==5.3.4
django-celery-beat==2.5.0
channels==4.0.0
channels-redis==4.1.0

# API Integrations
openai==1.3.5
google-api-python-client==2.108.0
google-auth-httplib2==0.1.1
google-auth-oauthlib==1.1.0
linkedin-api==2.0.0  # Custom wrapper
requests==2.31.0
beautifulsoup4==4.12.2

# Email Processing
imaplib2==3.6
email-reply-parser==0.5.12

# Data Processing
pandas==2.1.3
numpy==1.25.2
spacy==3.7.2

# Frontend
django-htmx==1.17.0
django-widget-tweaks==1.5.0
```

### Environment Configuration
```python
# .env
DJANGO_SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:pass@localhost/jobtracker
REDIS_URL=redis://localhost:6379/0

# API Keys
OPENAI_API_KEY=sk-...
LINKEDIN_CLIENT_ID=...
LINKEDIN_CLIENT_SECRET=...
XING_API_KEY=...
STEPSTONE_API_KEY=...
INDEED_PUBLISHER_ID=...
GLASSDOOR_PARTNER_ID=...

# Google APIs
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
GOOGLE_SHEETS_SCOPE=https://www.googleapis.com/auth/spreadsheets
GOOGLE_DOCS_SCOPE=https://www.googleapis.com/auth/documents

# Translation Services
LIBRETRANSLATE_URL=https://libretranslate.de
LIBRETRANSLATE_API_KEY=  # Optional for self-hosted instances
GOOGLE_TRANSLATE_API_KEY=  # Backup translation service
TRANSLATION_CACHE_TIMEOUT=86400  # 24 hours in seconds
DEFAULT_SOURCE_LANGUAGE=auto
DEFAULT_TARGET_LANGUAGE=en

# Language Settings
LANGUAGE_CODE=en-us
LANGUAGES=[('en', 'English'), ('de', 'German')]
USE_I18N=True
USE_L10N=True

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Translation Models Path (for offline Argos Translate)
ARGOS_TRANSLATE_MODELS_PATH=/app/translation_models/
```

### Frontend Implementation with Translation Support
```html
<!-- templates/dashboard/index.html -->
<div x-data="dashboard()" x-init="initTranslation()">
    <!-- Language selector -->
    <div class="language-selector">
        <select x-model="currentLanguage" @change="switchLanguage()">
            <option value="en">English</option>
            <option value="de">Deutsch</option>
            <option value="auto">Auto-detect</option>
        </select>
    </div>

    <!-- Real-time job statistics with translation -->
    <div class="stats-grid" hx-get="/api/dashboard-stats/" hx-trigger="every 30s">
        <!-- Auto-refreshing stats with language support -->
    </div>

    <!-- Job search and filtering with translation -->
    <div class="job-filters">
        <input type="text" x-model="search" @input.debounce.500ms="filterJobs()"
               :placeholder="translations.searchPlaceholder">
        <select x-model="platform" @change="filterJobs()">
            <option value="">All Platforms</option>
            <option value="linkedin">LinkedIn</option>
            <option value="xing">Xing</option>
            <option value="stepstone">StepStone</option>
            <option value="indeed">Indeed</option>
            <option value="glassdoor">Glassdoor</option>
        </select>

        <!-- Language filter for jobs -->
        <select x-model="jobLanguage" @change="filterJobs()">
            <option value="">All Languages</option>
            <option value="en">English Jobs</option>
            <option value="de">German Jobs</option>
        </select>
    </div>

    <!-- Job card with translation features -->
    <template x-for="job in filteredJobs" :key="job.id">
        <div class="job-card">
            <h3 x-text="job.title"></h3>
            <p x-text="job.company"></p>

            <!-- Translation controls -->
            <div class="translation-controls">
                <button @click="translateJobDescription(job.id, 'en')"
                        x-show="job.detected_language !== 'en'">
                    Translate to English
                </button>
                <button @click="translateJobDescription(job.id, 'de')"
                        x-show="job.detected_language !== 'de'">
                    Translate to German
                </button>
                <span x-text="'Original: ' + job.detected_language"
                      class="language-indicator"></span>
            </div>

            <!-- Job description with translation -->
            <div class="job-description">
                <div x-show="!job.showTranslation" x-text="job.description"></div>
                <div x-show="job.showTranslation" x-text="job.translated_description"></div>
                <button x-show="job.translated_description"
                        @click="job.showTranslation = !job.showTranslation"
                        x-text="job.showTranslation ? 'Show Original' : 'Show Translation'">
                </button>
            </div>
        </div>
    </template>

    <!-- AI-powered application assistant with language detection -->
    <div class="ai-assistant" x-show="showAssistant">
        <div class="language-detection">
            <span x-text="'Detected Language: ' + selectedJob.detected_language"></span>
            <select x-model="documentLanguage">
                <option value="auto">Auto (match job language)</option>
                <option value="en">English</option>
                <option value="de">German</option>
            </select>
        </div>

        <button @click="generateDocuments(selectedJob.id)"
                hx-post="/api/generate-documents/"
                hx-include="[name='language']"
                hx-indicator="#loading">
            Generate CV & Cover Letter
        </button>

        <input type="hidden" name="language" :value="documentLanguage">
    </div>

    <!-- Translation preview modal -->
    <div x-show="showTranslationModal" class="modal">
        <div class="modal-content">
            <h3>Translation Preview</h3>
            <div class="translation-comparison">
                <div class="original">
                    <h4>Original (<span x-text="originalLanguage"></span>)</h4>
                    <p x-text="originalText"></p>
                </div>
                <div class="translated">
                    <h4>Translated (<span x-text="targetLanguage"></span>)</h4>
                    <p x-text="translatedText"></p>
                </div>
            </div>
            <button @click="saveTranslation()">Save Translation</button>
            <button @click="showTranslationModal = false">Close</button>
        </div>
    </div>
</div>

<script>
function dashboard() {
    return {
        currentLanguage: 'en',
        documentLanguage: 'auto',
        jobLanguage: '',
        translations: {},
        jobs: [],
        filteredJobs: [],
        selectedJob: null,
        showTranslationModal: false,
        originalText: '',
        translatedText: '',
        originalLanguage: '',
        targetLanguage: '',

        initTranslation() {
            this.loadTranslations(this.currentLanguage);
        },

        async loadTranslations(language) {
            const response = await fetch(`/api/translations/${language}/`);
            this.translations = await response.json();
        },

        switchLanguage() {
            this.loadTranslations(this.currentLanguage);
            document.documentElement.lang = this.currentLanguage;
        },

        async translateJobDescription(jobId, targetLang) {
            const job = this.jobs.find(j => j.id === jobId);
            if (!job) return;

            try {
                const response = await fetch(`/api/jobs/${jobId}/translate_description/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': this.getCsrfToken()
                    },
                    body: JSON.stringify({
                        target_language: targetLang
                    })
                });

                const data = await response.json();
                job.translated_description = data.translated_description;
                job.translation_language = targetLang;
                job.showTranslation = true;

            } catch (error) {
                console.error('Translation failed:', error);
            }
        },

        filterJobs() {
            this.filteredJobs = this.jobs.filter(job => {
                const matchesSearch = !this.search ||
                    job.title.toLowerCase().includes(this.search.toLowerCase()) ||
                    job.company.toLowerCase().includes(this.search.toLowerCase());

                const matchesPlatform = !this.platform || job.platform === this.platform;
                const matchesLanguage = !this.jobLanguage || job.detected_language === this.jobLanguage;

                return matchesSearch && matchesPlatform && matchesLanguage;
            });
        },

        getCsrfToken() {
            return document.querySelector('[name=csrfmiddlewaretoken]').value;
        }
    }
}
</script>
```

## Testing Strategy

### Unit Tests
```python
# tests/test_ai_service.py
class TestAIContentService(TestCase):
    def setUp(self):
        self.ai_service = AIContentService()

    def test_cv_generation_german(self):
        # Test German CV generation with LibreTranslate
        job_description = "Wir suchen einen erfahrenen Python-Entwickler..."
        base_cv = "Experienced software developer with 5 years..."

        cv_content = self.ai_service.generate_cv(
            job_description, base_cv, target_language='de'
        )

        self.assertIn('Python', cv_content)
        # Verify German language in output

    def test_cover_letter_personalization(self):
        # Test job-specific cover letter generation

    def test_email_response_generation_multilingual(self):
        # Test automated email responses in multiple languages

    def test_language_detection(self):
        # Test automatic language detection
        translation_service = TranslationService()

        german_text = "Hallo, wie geht es Ihnen?"
        english_text = "Hello, how are you?"

        self.assertEqual(translation_service.detect_language(german_text), 'de')
        self.assertEqual(translation_service.detect_language(english_text), 'en')

# tests/test_translation_service.py
class TestTranslationService(TestCase):
    def setUp(self):
        self.translation_service = TranslationService()

    def test_libretranslate_integration(self):
        # Test LibreTranslate API integration
        text = "Hello world"
        translated = self.translation_service.translate(text, 'de', 'en')
        self.assertIn('Hallo', translated.lower())

    def test_argos_translate_offline(self):
        # Test offline translation with Argos
        argos_service = ArgosTranslateService()
        text = "Good morning"
        translated = argos_service.translate(text, 'de', 'en')
        self.assertIsNotNone(translated)

    def test_translation_caching(self):
        # Test translation cache functionality
        text = "Test caching"
        lang_pair = ('en', 'de')

        # First translation should hit API
        result1 = self.translation_service.translate(text, 'de', 'en')

        # Second should use cache
        result2 = self.translation_service.translate(text, 'de', 'en')

        self.assertEqual(result1, result2)

    def test_batch_translation(self):
        # Test batch translation efficiency
        documents = [
            "First document to translate",
            "Second document for translation",
            "Third document in the batch"
        ]

        results = self.translation_service.translate_document_batch(
            documents, 'de', 'en'
        )

        self.assertEqual(len(results), len(documents))

    def test_translation_fallback(self):
        # Test fallback to secondary translation services
        with patch('requests.post') as mock_post:
            mock_post.side_effect = Exception("LibreTranslate unavailable")

            # Should fallback to Google Translate or Argos
            result = self.translation_service.translate("Hello", 'de', 'en')
            self.assertIsNotNone(result)

# tests/test_job_scraping.py
class TestJobScrapingService(TestCase):
    def test_linkedin_job_extraction_multilingual(self):
        # Test LinkedIn API integration with language detection

    def test_german_job_board_integration(self):
        # Test Xing and StepStone German job extraction

    def test_duplicate_job_detection_across_languages(self):
        # Test deduplication logic for multilingual jobs

    def test_job_translation_automation(self):
        # Test automatic job description translation
```

### Integration Tests
```python
# tests/test_google_integration.py
class TestGoogleIntegration(TestCase):
    def test_sheets_export(self):
        # Test Google Sheets export functionality

    def test_docs_creation(self):
        # Test Google Docs CV/cover letter creation
```

## Deployment & Scaling

### Docker Configuration
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "job_tracker.wsgi:application"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/jobtracker
      - REDIS_URL=redis://redis:6379/0
      - LIBRETRANSLATE_URL=http://libretranslate:5000
    depends_on:
      - db
      - redis
      - libretranslate
    volumes:
      - ./translation_models:/app/translation_models

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: jobtracker
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

  # LibreTranslate service for private translation
  libretranslate:
    image: libretranslate/libretranslate:latest
    ports:
      - "5000:5000"
    environment:
      - LT_LOAD_ONLY=en,de  # Load only English and German models
      - LT_UPDATE_MODELS=true
    volumes:
      - lt_models:/app/db
    restart: unless-stopped

  celery:
    build: .
    command: celery -A job_tracker worker -l info
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/jobtracker
      - REDIS_URL=redis://redis:6379/0
      - LIBRETRANSLATE_URL=http://libretranslate:5000
    depends_on:
      - db
      - redis
      - libretranslate
    volumes:
      - ./translation_models:/app/translation_models

  celery-beat:
    build: .
    command: celery -A job_tracker beat -l info
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/jobtracker
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

volumes:
  postgres_data:
  lt_models:  # LibreTranslate models storage
```

## LibreTranslate Deployment Options

### Option 1: Use Public LibreTranslate Instance
```python
# settings.py
LIBRETRANSLATE_URL = "https://libretranslate.de"  # Free public instance
LIBRETRANSLATE_API_KEY = None  # Not required for public instance
```

### Option 2: Self-Hosted LibreTranslate
```bash
# Deploy your own LibreTranslate instance
docker run -d \
  --name libretranslate \
  -p 5000:5000 \
  -e LT_LOAD_ONLY=en,de \
  -e LT_UPDATE_MODELS=true \
  -v lt_models:/app/db \
  libretranslate/libretranslate:latest
```

### Option 3: Offline Translation with Argos
```python
# For completely offline operation
# Download language models during Docker build
RUN python -c "
import argostranslate.package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
for package in available_packages:
    if package.from_code in ['en', 'de'] and package.to_code in ['en', 'de']:
        package.install()
"
```

## Translation Performance Optimization

### 1. Caching Strategy
```python
# Translation caching for cost and performance optimization
from django.core.cache import cache
import hashlib

class TranslationService:
    def translate_with_cache(self, text, target_lang, source_lang='auto'):
        # Create cache key
        cache_key = f"translation:{hashlib.md5(text.encode()).hexdigest()}:{source_lang}:{target_lang}"

        # Check cache first
        cached_result = cache.get(cache_key)
        if cached_result:
            return cached_result

        # Perform translation
        result = self.translate(text, target_lang, source_lang)

        # Cache for 24 hours
        cache.set(cache_key, result, 86400)

        return result
```

### 2. Batch Processing
```python
# Efficient batch translation for large datasets
@shared_task
def translate_jobs_batch_task(job_ids, target_language):
    """Batch translate multiple jobs efficiently"""
    jobs = Job.objects.filter(id__in=job_ids)
    translation_service = TranslationService()

    # Group jobs by detected language for efficient batching
    jobs_by_language = {}
    for job in jobs:
        detected_lang = translation_service.detect_language(job.description)
        if detected_lang not in jobs_by_language:
            jobs_by_language[detected_lang] = []
        jobs_by_language[detected_lang].append(job)

    # Translate each language group in batch
    for source_lang, job_group in jobs_by_language.items():
        if source_lang != target_language:
            descriptions = [job.description for job in job_group]
            translated_descriptions = translation_service.translate_document_batch(
                descriptions, target_language, source_lang
            )

            # Update jobs with translations
            for job, translated_desc in zip(job_group, translated_descriptions):
                job.description_translated = translated_desc
                job.translation_language = target_language
                job.save()
```

## Security Considerations

1. **Translation Privacy**: Use self-hosted LibreTranslate for sensitive content
2. **API Rate Limiting**: Implement rate limiting for translation endpoints
3. **Content Filtering**: Validate translated content before saving
4. **Data Retention**: Set appropriate retention policies for translation cache
5. **Service Fallbacks**: Ensure graceful degradation when translation services fail

## Cost Optimization

### Translation Service Priority
1. **Primary**: Self-hosted LibreTranslate (free, private)
2. **Secondary**: Argos Translate (offline, free)
3. **Fallback**: Google Translate API (paid, reliable)

### Usage Monitoring
```python
# Track translation usage and costs
class TranslationUsage(models.Model):
    service_name = models.CharField(max_length=50)
    character_count = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    date = models.DateField(auto_now_add=True)

    @classmethod
    def log_usage(cls, service, text, cost=0):
        cls.objects.create(
            service_name=service,
            character_count=len(text),
            cost=cost
        )
```

## Security Considerations

1. **API Key Management**: Use environment variables and encryption for sensitive keys
2. **Email Security**: Implement OAuth2 for email access instead of passwords
3. **Rate Limiting**: Implement API rate limiting to prevent abuse
4. **Data Privacy**: GDPR compliance for storing personal data
5. **Authentication**: Use Django's built-in authentication with 2FA support

## Performance Optimization

1. **Database Indexing**: Index on frequently queried fields (job titles, companies, dates)
2. **Caching**: Redis caching for API responses and frequently accessed data
3. **Async Processing**: Use Celery for heavy operations (scraping, AI generation)
4. **API Optimization**: Implement pagination and filtering for large datasets
5. **CDN Integration**: Use CDN for static assets and document delivery

## Monitoring & Analytics

1. **Application Monitoring**: Implement logging and error tracking (Sentry)
2. **Performance Metrics**: Track API response times and database query performance
3. **Business Metrics**: Monitor application success rates and user engagement
4. **Cost Tracking**: Monitor API usage costs (OpenAI, Google APIs)

## Development Instructions for Cursor

1. **Start with core models**: Begin by implementing the database models and migrations
2. **API integrations first**: Implement job platform APIs with proper error handling
3. **AI service implementation**: Create the OpenAI integration for content generation
4. **Email processing**: Build email parsing and automated response system
5. **Google integrations**: Implement Google Sheets and Docs API connections
6. **Frontend development**: Use HTMX for dynamic updates and Alpine.js for interactivity
7. **Testing**: Write comprehensive tests for each integration
8. **Deployment setup**: Configure Docker and environment variables

## Success Metrics

- **Job Discovery**: Successfully scrape and track 1000+ jobs daily across all platforms
- **Application Efficiency**: Generate personalized CVs and cover letters in under 30 seconds
- **Email Automation**: Achieve 80%+ automated email response rate
- **Success Tracking**: Provide actionable insights to improve application success rates
- **Multi-language Support**: Seamless German and English document generation
```
