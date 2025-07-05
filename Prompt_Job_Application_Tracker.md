# Prompt_Job_Application_Tracker.md

## Project Context for Cursor AI Assistant

### Project Overview
Django-based Job Application Tracker with AI-powered CV/cover letter generation, multi-platform job scraping (LinkedIn, Xing, 
StepStone, Indeed, Glassdoor), automated email responses, and Google Workspace integration. Supports German and English languages.

### Tech Stack Rules
- **Backend**: Django 4.2+ with DRF, PostgreSQL, Redis, Celery
- **Frontend**: HTMX + Alpine.js + Tailwind CSS (no React/Vue)
- **AI**: OpenAI GPT-4 for content generation
- **APIs**: Google Sheets/Docs, LinkedIn, Xing, StepStone, Indeed, Glassdoor
- **Email**: SMTP with tracking and AI-generated responses

---

## Cursor Prompt Templates

### 1. Django Model Creation
```
Create Django models for [model_name] with the following requirements:
- Include proper relationships and indexes
- Add validation for German/English fields
- Include audit fields (created_at, updated_at)
- Follow Django best practices for naming
- Add Meta class with proper ordering
- Include __str__ method for admin interface

Context: Job Application Tracker with multi-language support
```

### 2. API Integration Service
```
Create a service class for [platform_name] API integration:
- Implement authentication handling
- Add rate limiting and error handling
- Include data transformation methods
- Add caching for repeated requests
- Support pagination for large datasets
- Include unit tests for all methods

Platform: [LinkedIn/Xing/StepStone/Indeed/Glassdoor]
Data format: Jobs, company info, salary data
```

### 3. OpenAI Content Generation
```
Create an OpenAI service for generating [content_type]:
- Support German and English languages
- Include prompt engineering for professional tone
- Add content personalization based on job requirements
- Implement token usage optimization
- Include error handling and fallbacks
- Add content validation and formatting

Content type: [CV/Cover Letter/Email Response/Follow-up Email]
Target audience: German job market
```

### 4. Email Automation System
```
Build email automation service with:
- Template-based email generation
- AI-powered personalization using OpenAI
- SMTP configuration with tracking pixels
- Scheduled sending with Celery
- Open/click/reply tracking
- German/English template support
- Integration with job application workflow

Email types: Follow-up, Thank you, Interview request, Status inquiry
```

### 5. Web Scraping Implementation
```
Create web scraper for [job_platform]:
- Use Selenium/BeautifulSoup for dynamic content
- Implement anti-bot detection avoidance
- Add data cleaning and normalization
- Include duplicate detection logic
- Support pagination and bulk processing
- Add error handling and retry mechanisms
- Store scraped data in Django models

Platform: [StepStone/Indeed/Xing careers page]
Target data: Job title, company, location, description, requirements, salary
```

### 6. Google Workspace Integration
```
Implement Google [Sheets/Docs] integration:
- OAuth2 authentication flow
- Service account setup for automation
- CRUD operations for spreadsheets/documents
- Real-time data synchronization
- Error handling for API limits
- Batch operations for efficiency
- Integration with Django models

Use case: Export job applications / Generate CV documents
Data flow: Django → Google Workspace → User access
```

### 7. Analytics Dashboard
```
Create analytics dashboard component:
- Chart.js/Plotly integration
- Real-time data updates with HTMX
- Performance metrics calculation
- Market analysis visualization
- Export functionality to PDF/Excel
- Mobile-responsive design with Tailwind
- Filter and date range selection

Metrics: Application success rate, response times, platform performance, salary trends
```

### 8. Celery Task Implementation
```
Create Celery task for [task_name]:
- Implement task with proper error handling
- Add progress tracking and logging
- Include retry logic with exponential backoff
- Add task result storage
- Implement task monitoring
- Include proper cleanup after completion

Task type: [Job scraping/Email sending/Report generation/Data synchronization]
Schedule: [Hourly/Daily/Weekly/On-demand]
```

### 9. HTMX Dynamic Component
```
Create HTMX-powered component for [feature_name]:
- Dynamic content loading without page refresh
- Form handling with server-side validation
- Real-time updates using SSE or polling
- Error handling with user feedback
- Loading states and animations
- Integration with Alpine.js for client-side logic
- Tailwind CSS for responsive styling

Feature: [Job search/Application tracking/Document preview/Analytics filters]
```

### 10. Django REST API Endpoint
```
Create DRF viewset/serializer for [model_name]:
- Include proper permissions and authentication
- Add filtering, searching, and pagination
- Implement field-level validation
- Add API documentation with swagger
- Include rate limiting
- Add request/response logging
- Support for German/English content

Model: [Job/JobApplication/EmailCampaign/CompanyInsight]
Access level: [Authenticated users only/Admin only/Public read]
```

### 11. Database Optimization
```
Optimize database queries for [feature_name]:
- Add proper select_related/prefetch_related
- Create database indexes for frequent queries
- Implement query caching with Redis
- Add database connection pooling
- Optimize N+1 query problems
- Add query performance monitoring

Feature: [Job search/Application listing/Analytics dashboard/Email tracking]
Expected load: [100+ concurrent users/10k+ records]
```

### 12. Authentication & Security
```
Implement security feature for [component_name]:
- Add proper authentication checks
- Implement CSRF protection
- Add rate limiting for API endpoints
- Include input validation and sanitization
- Add audit logging for sensitive operations
- Implement proper error handling without information leakage

Component: [API endpoints/File uploads/Email processing/External API calls]
Security level: [Standard/High security/PII handling]
```

### 13. Testing Implementation
```
Create comprehensive tests for [component_name]:
- Unit tests for all methods
- Integration tests for API endpoints
- Mock external API calls
- Test German/English content generation
- Add performance tests for heavy operations
- Include edge case testing
- Add CI/CD pipeline configuration

Component: [Email service/API integration/Scraping service/Analytics]
Coverage target: 90%+
```

### 14. Multi-language Support
```
Implement internationalization for [feature_name]:
- Django i18n setup for German/English
- Database fields for multilingual content
- Template translation strings
- Dynamic language switching
- Currency and date localization
- Email template translations
- URL pattern localization

Feature: [Job descriptions/Email templates/UI interface/Generated documents]
Languages: German (primary), English (secondary)
```

### 15. Error Handling & Logging
```
Implement robust error handling for [service_name]:
- Custom exception classes
- Structured logging with correlation IDs
- Error notification system
- Graceful degradation for external API failures
- User-friendly error messages
- Performance monitoring integration
- Health check endpoints

Service: [Email automation/Job scraping/AI content generation/Google API integration]
Monitoring: [Sentry/Django logging/Custom dashboard]
```

---

## Django-Rules Specific Prompts

### 16. Permission System
```
Implement django-rules permissions for [feature_name]:
- Define predicates for user access control
- Add object-level permissions
- Implement role-based access (Admin/User/Viewer)
- Add conditional permissions based on subscription
- Include permission testing in views
- Add permission checks in templates

Feature: [Job applications/Email campaigns/Analytics/API access]
Roles: Owner, Collaborator, Viewer
```

### 17. Business Logic Rules
```
Create django-rules for [business_logic]:
- Define complex business rules as predicates
- Implement conditional logic for automation
- Add time-based rules (trial periods, subscriptions)
- Include geographic restrictions for job platforms
- Add usage limits and quota management
- Implement approval workflows

Logic: [Email sending limits/API rate limiting/Feature access/Content generation quotas]
```

---

## File Structure Templates

### Project Structure Prompt
```
Generate Django project structure following these conventions:
- apps/ directory for all Django apps
- config/ for settings and environment configs
- static/ and media/ for assets
- templates/ with app-specific subdirectories
- requirements/ directory with env-specific files
- docker/ directory for containerization
- scripts/ for management commands
- tests/ directory structure matching apps/

Include: __init__.py files, proper imports, basic configurations
```

### App Structure Prompt
```
Create Django app structure for [app_name]:
- models.py with proper relationships
- views.py with class-based views
- serializers.py for DRF
- services.py for business logic
- tasks.py for Celery operations
- admin.py with proper ModelAdmin
- urls.py with proper namespacing
- tests/ directory with test files

App purpose: [Job management/Email automation/Analytics/API integration]
```

---

## Code Quality Rules

### Code Style Prompt
```
Ensure code follows these standards:
- Black formatter for Python code
- isort for import organization
- flake8 for linting with max line length 88
- Type hints for all function parameters and returns
- Docstrings for all classes and methods
- German comments for business logic
- English comments for technical implementation
```

### Django Best Practices Prompt
```
Apply Django best practices:
- Use class-based views over function-based
- Implement proper model validation
- Use select_related/prefetch_related for optimization
- Add proper middleware for security
- Use Django forms for validation
- Implement proper error handling
- Add database migrations for all model changes
- Use Django's built-in authentication system
```

---

## Deployment & DevOps Prompts

### Docker Configuration
```
Create Docker setup for development/production:
- Multi-stage Dockerfile for optimization
- docker-compose.yml with all services
- Environment-specific configurations
- Health checks for all services
- Volume mounts for development
- Production-ready security settings
- Database initialization scripts

Services: Django, PostgreSQL, Redis, Celery Worker, Celery Beat, Nginx
```

### CI/CD Pipeline
```
Create GitHub Actions workflow:
- Automated testing on pull requests
- Code quality checks (black, isort, flake8)
- Security scanning with bandit
- Database migration testing
- Docker image building and pushing
- Deployment to staging/production
- Performance testing for critical paths

Environments: Development, Staging, Production
```

---

## Usage Instructions for Cursor

1. **Copy the relevant prompt** from above based on your current task
2. **Customize the bracketed placeholders** [model_name], [platform_name], etc.
3. **Add specific requirements** to the prompt based on your needs
4. **Paste into Cursor** and let the AI generate the code
5. **Review and refine** the generated code following Django best practices

### Example Usage:
```
Take prompt #3 (OpenAI Content Generation) and customize:
- Replace [content_type] with "Cover Letter"
- Add specific requirements for German job market
- Specify the job application context
```

### Pro Tips:
- Always specify the German/English language requirement
- Include the context of job application tracking
- Mention integration with existing models when relevant
- Ask for tests and documentation when generating services
- Request proper error handling for external API integrations
