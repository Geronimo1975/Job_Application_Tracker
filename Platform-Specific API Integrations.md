### Platform-Specific API Integrations
```python
# integrations/apis.py
class LinkedInAPI:
    def __init__(self, access_token):
        self.client = linkedin.LinkedInApplication(token=access_token)

    def search_jobs(self, keywords, location, limit=50):
        # LinkedIn Jobs API integration
        pass

    def get_company_info(self, company_id):
        # Company insights and employee data
        pass

class XingAPI:
    def __init__(self, consumer_key, consumer_secret):
        self.client = xing.XingAPI(consumer_key, consumer_secret)

    def search_jobs(self, keywords, location):
        # Xing Jobs API integration
        pass

class StepStoneAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_jobs(self, search_params):
        # StepStone API integration
        pass

class IndeedAPI:
    def __init__(self, publisher_id):
        self.publisher_id = publisher_id

    def job_search(self, query, location):
        # Indeed API integration
        pass

class GlassdoorAPI:
    def __init__(self, partner_id, key):
        self.partner_id = partner_id
        self.key = key

    def get_salary_data(self, job_title, location):
        # Salary insights and company reviews
        pass
```

### Email Integration Models
```python
# integrations/models.py
class EmailTemplate(models.Model):
    TEMPLATE_TYPES = [
        ('follow_up', 'Follow Up'),
        ('thank_you', 'Thank You'),
        ('interview_request', 'Interview Request'),
        ('status_inquiry', 'Status Inquiry'),
    ]

    name = models.CharField(max_length=100)
    template_type = models.CharField(max_length=20, choices=TEMPLATE_TYPES)
    subject_template = models.CharField(max_length=200)
    body_template = models.TextField()
    language = models.CharField(max_length=2, choices=[('en', 'English'), ('de', 'German')])

class EmailCampaign(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    recipient_email = models.EmailField()
    sent_at = models.DateTimeField(null=True, blank=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    clicked_at = models.DateTimeField(null=True, blank=True)
    replied_at = models.DateTimeField(null=True, blank=True)

class AIEmailResponse(models.Model):
    original_email = models.TextField()
    generated_response = models.TextField()
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    language = models.CharField(max_length=2)
    tone = models.CharField(max_length=20)  # professional, friendly, formal
    approved = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
```

### Analytics & Reporting Models
```python
# analytics/models.py
class MarketAnalysis(models.Model):
    skill_name = models.CharField(max_length=100)
    demand_score = models.FloatField()
    average_salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    analysis_date = models.DateTimeField(auto_now_add=True)

class ApplicationMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_applications = models.IntegerField()
    interview_rate = models.FloatField()
    response_rate = models.FloatField()# Django Job Application Tracker - Cursor Development Prompt

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

### 4. Advanced Analytics & API Pipeline
- **Multi-Platform Integration**: Direct API connections to LinkedIn, Xing, StepStone, Indeed, and Glassdoor
- **Real-time Data Synchronization**: Automated job fetching and status updates
- **Market Analysis**: Salary trends, skill demand analysis, and company insights
- **Performance Metrics**: Application success rates, response times, and conversion analytics
- **Competitive Intelligence**: Track similar positions and market saturation

### 5. Email Integration & AI Responses
- **Email Automation**:
  - Send personalized follow-up emails after applications
  - Automated thank-you emails after interviews
  - Reminder emails for pending applications
- **AI-Powered Responses**:
  - Generate personalized email responses to recruiter inquiries
  - Craft follow-up messages based on application status
  - Create interview scheduling emails
  - Multi-language email generation (German/English)
- **Email Tracking**: Monitor email opens, clicks, and responses

### 6. Web Interface
- **Dashboard**: Overview of applications, success rates, and upcoming deadlines
- **Job Management**: Add, edit, and track job applications
- **Document Preview**: View and edit generated documents
- **Analytics**: Charts showing application trends and success rates
- **Email Center**: Manage automated emails and AI responses

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

### Key Models
```python
# jobs/models.py
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    requirements = models.TextField()
    url = models.URLField(unique=True)
    source = models.CharField(max_length=50)  # stepstone, xing, etc.
    posted_date = models.DateTimeField()
