# Online Judge Development Platform

A comprehensive online judge system built with Django and Django REST Framework for competitive programming and coding assessments.

## 🏆 Features

- **User Authentication & Authorization** - JWT-based authentication system
- **Problem Management** - Create, manage, and categorize coding problems
- **Contest System** - Organize programming contests with time limits
- **Code Submission & Judging** - Multi-language support for code evaluation
- **Rating System** - Track user performance and ratings
- **Team Competitions** - Support for team-based contests
- **Institution Management** - Organize users by educational institutions
- **Real-time Announcements** - Contest announcements and Q&A system

## 🚀 Tech Stack

- **Backend**: Django 5.2.3, Django REST Framework
- **Authentication**: Django REST Framework Simple JWT
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Task Queue**: Celery with Redis
- **Additional Libraries**:
  - `django-phonenumber-field` - Phone number validation
  - `django-colorfield` - Color field support for ratings

## 📁 Project Structure

```
OnlineJudgeDev/
├── OnlineJudge/                 # Main Django project
│   ├── manage.py               # Django management script
│   ├── db.sqlite3              # SQLite database
│   ├── requirements.txt        # Python dependencies
│   │
│   ├── OnlineJudge/            # Project settings
│   │   ├── settings.py         # Main configuration
│   │   ├── urls.py             # URL routing
│   │   ├── wsgi.py             # WSGI configuration
│   │   └── asgi.py             # ASGI configuration
│   │
│   ├── Accounts/               # User authentication & management
│   ├── Contest/                # Contest management system
│   ├── Institution/            # Educational institutions
│   ├── Judge/                  # Code judging system
│   ├── Problem/                # Problem repository
│   ├── Profile/                # User profiles
│   ├── Rating/                 # Rating & ranking system
│   ├── Submission/             # Code submissions
│   ├── Tag/                    # Problem categorization
│   └── Team/                   # Team management
│
├── Scripts/                    # API testing scripts
├── DocumentsOfDevelopers/      # Development documentation
├── malo-01/                    # Frontend assets
└── README.md                   # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+ (tested with Python 3.13)
- pip (Python package manager)
- Redis (for Celery task queue)
- Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd OnlineJudgeDev
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
cd OnlineJudge
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file in the `OnlineJudge` directory (optional, for production):

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_URL=redis://localhost:6379/0
```

### 5. Database Setup

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 6. Start Redis Server

```bash
# Windows (if Redis is installed)
redis-server

# Linux/Mac
sudo systemctl start redis
# or
redis-server
```

### 7. Start Celery Worker (Optional)

```bash
# In a separate terminal
celery -A OnlineJudge worker --loglevel=info
```

### 8. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 🔗 API Endpoints

### Authentication
- `POST /api/auth/` - User login
- `POST /api/auth/register/` - User registration
- `POST /api/auth/token/` - Get JWT token
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `POST /api/auth/token/verify/` - Verify JWT token

### Core Features
- `GET/POST /api/profile/` - User profile management
- `GET/POST /api/contests/` - Contest operations
- `GET/POST /api/problems/` - Problem management
- `GET/POST /api/submissions/` - Code submissions

## 🧪 Testing

Run the API tests using the provided scripts:

```bash
# Test user API
python Scripts/User_API_Test.py

# Test profile API
python Scripts/Profile_API_Test.py
```

## 📚 Development Documentation

Detailed development documentation is available in the `DocumentsOfDevelopers/` directory:

- `Features(Project Online Judge).docx` - Complete feature specifications
- `Guide.txt` - Development guide
- `howToRun.txt` - Setup instructions
- `relational-schema.jpg` - Database schema
- `countries.txt` - Supported countries list

## 🏗️ Architecture

### Apps Overview

1. **Accounts** - User authentication, registration, JWT token management
2. **Profile** - User profiles with personal information and institution links
3. **Contest** - Contest creation, management, announcements, and Q&A
4. **Problem** - Problem repository with descriptions and test cases
5. **Judge** - Code execution and evaluation system
6. **Submission** - Code submission handling and result storage
7. **Rating** - User rating calculation and leaderboards
8. **Team** - Team formation and team-based contests
9. **Institution** - Educational institution management
10. **Tag** - Problem categorization and filtering

### Key Models

- **User** (Django built-in) - Authentication
- **Profile** - Extended user information
- **Contest** - Contest details and timing
- **Problem** - Coding problems
- **Submission** - User code submissions
- **Rating_Change** - Rating history tracking

## 🔧 Configuration

### JWT Settings

The project uses Django REST Framework Simple JWT with the following configuration:

```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('JWT',),
}
```

### Celery Settings

Background task processing is configured with Redis:

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

## 🚀 Deployment

### Production Checklist

1. Set `DEBUG = False` in settings
2. Configure proper `ALLOWED_HOSTS`
3. Use PostgreSQL database
4. Set up proper static file serving
5. Configure Celery with production Redis
6. Set up proper logging
7. Use environment variables for sensitive data

### Docker Deployment (Recommended)

A `Dockerfile` and `docker-compose.yml` can be added for containerized deployment.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed in your virtual environment
2. **Database Errors**: Run migrations if you encounter database-related issues
3. **JWT Errors**: Check if Redis is running for proper token management
4. **Port Conflicts**: Change the port using `python manage.py runserver 8080`

### Support

For issues and questions:
1. Check the development documentation in `DocumentsOfDevelopers/`
2. Review the error logs in the console
3. Open an issue in the repository

## 🎯 Roadmap

- [ ] Docker containerization
- [ ] Advanced problem difficulty algorithms
- [ ] Real-time contest leaderboards
- [ ] Code plagiarism detection
- [ ] Multi-language judge support expansion
- [ ] Performance optimization
- [ ] Enhanced UI/UX improvements

---

**Happy Coding!** 🎉