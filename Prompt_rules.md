# 🚀 Prompt_MCP.md - Ghid Personalizat pentru Django + AI + Automation Stack

> **Configurat conform User Rules și Project Rules din Cursor**
> 
> Stack: Django + PostgreSQL + Docker + Nginx + Gunicorn + AI/RAG + n8n/Make.com + GitHub Actions

## 📋 Cuprins
- [User Rules Compliant Prompts](#user-rules-compliant-prompts)
- [Project-Specific Development](#project-specific-development)
- [Django MVT Architecture](#django-mvt-architecture)
- [AI/RAG System Management](#airag-system-management)
- [Automation Workflows](#automation-workflows)
- [Security & Quality Standards](#security--quality-standards)
- [CI/CD & Deployment](#cicd--deployment)
- [Code Quality & Testing](#code-quality--testing)

---

## 🎯 User Rules Compliant Prompts

*These prompts follow your configured User Rules for Django best practices, security, and code quality*

### Django Development with Best Practices
```
Create a Django class-based view for user profile management with proper error handling, security validation, and comprehensive docstrings 
following PEP 8 standards
```
**Ensures**: Class-based views, security patterns, documentation standards

```
Build a Django model with proper field validation, database constraints, and type hints including comprehensive unit tests
```
**Ensures**: Django ORM best practices, validation, testing requirements

```
Implement Django form with CSRF protection, input validation, and error handling using Django's built-in security features
```
**Ensures**: Security-first approach, built-in Django features

### Production-Ready Code Standards
```
Write production-ready Django API endpoint with rate limiting, authentication, proper error responses, logging, and OpenAPI documentation
```
**Ensures**: Production standards, comprehensive error handling, documentation

```
Create Django middleware with proper logging, error handling, type hints, and unit tests following security best practices
```
**Ensures**: Code quality standards, security considerations, testing

```
Implement Django custom management command with argument validation, progress tracking, logging, and comprehensive error handling
```
**Ensures**: Robust command-line tools, proper error handling

---

## 🏗️ Project-Specific Development

*These prompts align with your Project Rules for MVT architecture, AI integration, and automation*

### Django MVT Architecture Compliance
```
Design Django app following MVT architecture with proper separation of concerns, using class-based views and Django ORM for [specific 
functionality]
```
**Project Rule**: Follows Django MVT architecture with PostgreSQL

```
Create Django template with proper template inheritance, context processors, and static file management following project structure
```
**Project Rule**: MVT architecture compliance

```
Implement Django URL patterns with proper namespacing, regex patterns, and view mapping following RESTful principles
```
**Project Rule**: Django best practices and architecture

### AI/RAG Core Feature Integration
```
Implement AI chatbot integration with vector database management, efficient embedding operations, and fallback mechanisms for service failures
```
**Project Rule**: AI chatbot and RAG are core features

```
Create RAG document indexing system with PostgreSQL vector extension, embedding management, and efficient similarity search
```
**Project Rule**: Vector databases and embedding management

```
Build AI model response handler with proper error handling, rate limiting, caching, and fallback to default responses
```
**Project Rule**: AI service failure fallbacks

### Automation Webhook Architecture
```
Create robust n8n webhook endpoint with authentication, input validation, retry logic, and structured error responses designed for idempotent 
operations
```
**Project Rule**: n8n/Make.com robust webhook integration

```
Implement Make.com automation trigger with proper authentication, input sanitization, exponential backoff retry, and comprehensive logging
```
**Project Rule**: Automation workflows integration

```
Design webhook payload validation system with schema validation, error responses, and audit logging for automation workflows
```
**Project Rule**: Idempotent operations and validation

---

## 🐳 Docker & Production Deployment

*Following your deployment stack rules: Docker + Nginx + Gunicorn + GitHub Actions*

### Docker Container Management
```
Create Docker multi-stage build for Django application with security scanning, health checks, and production optimization
```
**Project Rule**: Docker containers with Nginx + Gunicorn

```
Implement Docker Compose configuration for Django stack with PostgreSQL, Redis, Nginx, and proper volume management for staging/production
```
**Project Rule**: Deployment stack compliance

```
Design Dockerfile with security best practices, minimal attack surface, and health check endpoints
```
**Project Rule**: Security and deployment standards

### GitHub Actions CI/CD Pipeline
```
Create GitHub Actions workflow for Django CI/CD with database migrations, testing, security scanning, and zero-downtime deployment to 
staging/production
```
**Project Rule**: GitHub Actions for CI/CD with environments

```
Implement GitHub Actions deployment pipeline with database backup, rollback strategy, and environment-specific configurations
```
**Project Rule**: Database backups and rollback strategies

```
Design GitHub Actions security workflow with dependency scanning, SAST analysis, and deployment approval gates for production
```
**Project Rule**: Security scanning and approval processes

---

## 🤖 AI/RAG System Management

*Specialized prompts for your AI chatbot and RAG implementation*

### Vector Database Operations
```
Implement PostgreSQL vector extension setup with pgvector for efficient similarity search, index optimization, and query performance monitoring
```
**Technical Focus**: Vector database efficiency

```
Create embedding generation pipeline with batch processing, error handling, and efficient storage in PostgreSQL vector columns
```
**Technical Focus**: Embedding management

```
Design RAG retrieval system with semantic search, relevance scoring, and context window optimization for AI responses
```
**Technical Focus**: RAG system optimization

### AI Model Integration
```
Implement AI model API integration with rate limiting, response caching, error handling, and cost monitoring for production use
```
**Technical Focus**: Production AI integration

```
Create AI chatbot conversation management with context preservation, session handling, and response quality monitoring
```
**Technical Focus**: Chatbot conversation flow

```
Design AI model fallback system with multiple provider support, graceful degradation, and response quality assessment
```
**Technical Focus**: AI reliability and fallbacks

---

## ⚡ Automation & Integration

*n8n and Make.com integration prompts following your automation rules*

### n8n Workflow Integration
```
Create Django webhook receiver for n8n with authentication via API keys, input validation using Django forms, and structured JSON responses
```
**Integration Focus**: n8n webhook integration

```
Implement n8n trigger endpoint with idempotent operation design, duplicate detection, and comprehensive audit logging
```
**Integration Focus**: Idempotent automation operations

```
Design n8n data transformation endpoint with schema validation, error handling, and retry mechanism for failed operations
```
**Integration Focus**: Robust data processing

### Make.com Scenario Integration
```
Build Make.com webhook handler with proper authentication, input sanitization, rate limiting, and response formatting
```
**Integration Focus**: Make.com integration

```
Create Make.com automation trigger with payload validation, error responses, and integration with Django models
```
**Integration Focus**: Model integration with automation

```
Implement Make.com data sync endpoint with conflict resolution, data validation, and comprehensive logging
```
**Integration Focus**: Data synchronization

---

## 🔒 Security & Quality Standards

*Following your code quality rules: PEP 8, type hints, testing, security*

### Security Implementation
```
Implement Django security middleware with rate limiting, request validation, security headers, and comprehensive logging of security events
```
**Security Focus**: Comprehensive security implementation

```
Create Django authentication system with multi-factor authentication, session management, and security event monitoring
```
**Security Focus**: Advanced authentication

```
Design Django API security with JWT tokens, rate limiting, input validation, and security audit logging
```
**Security Focus**: API security best practices

### Code Quality & Testing
```
Write comprehensive Django unit tests with >80% coverage, including model tests, view tests, form validation tests, and integration tests
```
**Quality Focus**: Testing requirements (>80% coverage)

```
Create Django code with type hints, comprehensive docstrings, PEP 8 compliance, and proper error handling for all functions
```
**Quality Focus**: Code quality standards

```
Implement Django logging system with structured logging, error tracking, performance monitoring, and security event logging
```
**Quality Focus**: Logging and monitoring standards

---

## 🚀 Performance & Optimization

*Database optimization and caching following your performance rules*

### Database Optimization
```
Optimize Django PostgreSQL queries with proper indexing, select_related/prefetch_related usage, and query performance monitoring
```
**Performance Focus**: Database optimization

```
Implement Django caching strategy with Redis, cache invalidation, and performance monitoring for high-traffic endpoints
```
**Performance Focus**: Caching optimization

```
Create Django database connection pooling with pgbouncer, monitoring, and performance tuning for production workloads
```
**Performance Focus**: Connection management

### Application Performance
```
Implement Django background task processing with Celery, Redis broker, monitoring, and error handling for long-running operations
```
**Performance Focus**: Background processing

```
Create Django API response optimization with pagination, field selection, compression, and response time monitoring
```
**Performance Focus**: API optimization

```
Design Django static file serving with CDN integration, compression, and cache optimization for production deployment
```
**Performance Focus**: Static file optimization

---

## 🔧 Development Workflows

*Quick development commands following your alias configurations*

### Rapid Development
```
Start complete development environment with database, Redis, and all services using Docker Compose for immediate development
```
**Workflow**: `dev` alias - Complete development setup

```
Run comprehensive test suite with coverage reporting, parallel execution, and performance profiling
```
**Workflow**: `test` alias - Testing workflow

```
Execute database migration workflow with backup, migration, and verification steps
```
**Workflow**: `mig` alias - Database management

### CI/CD Operations
```
Execute complete CI pipeline with testing, security scanning, and deployment preparation
```
**Workflow**: `ci` alias - Continuous integration

```
Deploy to staging environment with database migration, static file collection, and service verification
```
**Workflow**: `staging` alias - Staging deployment

```
Execute production deployment with backup, zero-downtime deployment, and rollback preparation
```
**Workflow**: `prod` alias - Production deployment

---

## 💡 Context-Aware Examples

*Practical examples following your configured rules and project structure*

### Complete Feature Development
```
Create user authentication feature with:
1. Django class-based views with proper error handling
2. PostgreSQL models with constraints and indexes
3. Comprehensive unit tests with >80% coverage
4. AI integration for user behavior analysis
5. n8n webhook for user lifecycle events
6. GitHub Actions deployment pipeline
7. Security audit and logging implementation
```

### AI System Enhancement
```
Enhance RAG system with:
1. Vector database optimization for similarity search
2. Embedding pipeline with batch processing
3. AI model integration with fallback mechanisms
4. Performance monitoring and cost tracking
5. Integration with automation workflows
6. Comprehensive error handling and logging
```

### Automation Workflow Implementation
```
Build automation integration with:
1. Robust webhook endpoints with authentication
2. Input validation and sanitization
3. Idempotent operation design
4. Retry logic with exponential backoff
5. Comprehensive audit logging
6. Error handling and response formatting
7. Integration testing with external services
```

---

## 📊 Monitoring & Maintenance

*System monitoring following your operational requirements*

### Health Monitoring
```
Implement comprehensive system health monitoring with Django health checks, database monitoring, AI service monitoring, and automation workflow 
tracking
```

### Performance Analytics
```
Create performance dashboard with Django query analysis, AI response times, automation success rates, and system resource monitoring
```

### Security Auditing
```
Implement security audit system with Django security checks, vulnerability scanning, access logging, and compliance reporting
```

---

## 🎯 Quick Reference Commands

### Development
- `"Start complete development environment"` → Full dev setup
- `"Run comprehensive test suite"` → Complete testing
- `"Execute database migration workflow"` → DB management

### AI System
- `"Update RAG system with new documents"` → AI system update
- `"Optimize vector database performance"` → Vector optimization
- `"Monitor AI service costs and usage"` → AI monitoring

### Automation
- `"Test all automation webhook endpoints"` → Automation testing
- `"Deploy automation workflow updates"` → Automation deployment
- `"Monitor automation success rates"` → Automation monitoring

### Production
- `"Execute zero-downtime production deployment"` → Production deploy
- `"Create database backup and verification"` → Backup operations
- `"Monitor system health and performance"` → System monitoring

---

**📝 Note**: All prompts are specifically designed to follow your configured User Rules and Project Rules in Cursor, ensuring consistent, 
high-quality, secure, and well-tested code that aligns with your Django + AI + Automation stack architecture.xy
