===================================================
TEAM TASK MANAGER - Full Stack Django Web App
===================================================

TECH STACK:
  - Backend: Django 4.2 + Django REST Framework
  - Database: PostgreSQL (Railway) / SQLite (local)
  - Auth: Session-based (Web UI) + JWT (REST API)
  - Frontend: Django Templates + Bootstrap 5
  - Deployment: Railway

FEATURES:
  - Role-based access: Admin / Member
  - Signup, Login, Logout with validation
  - Project creation, editing, deletion
  - Task management with status tracking (Todo / In Progress / Done)
  - Priority levels (Low / Medium / High)
  - Overdue task tracking
  - Dashboard with stats
  - Full REST API with JWT auth
  - Admin panel at /admin/

REST API ENDPOINTS:
  POST   /api/token/           -> Get JWT token (login)
  POST   /api/token/refresh/   -> Refresh JWT token
  POST   /api/register/        -> Register new user
  GET    /api/users/           -> List users
  GET    /api/users/me/        -> Current user info
  CRUD   /api/projects/        -> Projects API
  CRUD   /api/tasks/           -> Tasks API
  GET    /api/tasks/overdue/   -> Overdue tasks
  GET    /api/tasks/my_tasks/  -> My assigned tasks

=====================================================
LOCAL SETUP (Ubuntu/Linux)
=====================================================

1. INSTALL DEPENDENCIES
   sudo apt update
   sudo apt install python3 python3-pip python3-venv git -y

2. CLONE / EXTRACT PROJECT
   cd ~
   # If from zip: unzip team_task_manager.zip
   # If from git: git clone <your-repo-url>
   cd team_task_manager

3. CREATE VIRTUAL ENVIRONMENT
   python3 -m venv venv
   source venv/bin/activate

4. INSTALL PYTHON PACKAGES
   pip install -r requirements.txt

5. SET UP ENVIRONMENT VARIABLES
   cp .env.example .env
   # Edit .env file:
   nano .env
   # Set a strong SECRET_KEY (required)

6. RUN MIGRATIONS
   python manage.py migrate

7. CREATE SUPERUSER (Admin account)
   python manage.py createsuperuser
   # Enter username, email, password when prompted

8. COLLECT STATIC FILES (optional for local)
   python manage.py collectstatic --no-input

9. RUN THE SERVER
   python manage.py runserver

10. OPEN IN BROWSER
    http://localhost:8000/

=====================================================
RAILWAY DEPLOYMENT
=====================================================

1. Create account at https://railway.app

2. Push your code to GitHub:
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-url>
   git push -u origin main

3. On Railway:
   - Click "New Project" > "Deploy from GitHub repo"
   - Select your repository
   - Add a PostgreSQL plugin/service

4. Set Environment Variables in Railway:
   SECRET_KEY    = <generate-strong-key>
   DEBUG         = False
   DATABASE_URL  = (auto-set by Railway PostgreSQL plugin)
   ALLOWED_HOSTS = your-app.railway.app

5. Railway will auto-run:
   python manage.py migrate
   python manage.py collectstatic --no-input
   gunicorn team_task_manager.wsgi

6. After deploy, create superuser via Railway console:
   python manage.py createsuperuser

GENERATE A SECRET KEY (run in Python):
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

=====================================================
ROLES EXPLAINED
=====================================================

ADMIN:
  - Can view, edit, delete ALL projects and tasks
  - Can manage all users
  - Access to /admin/ panel

MEMBER:
  - Can create/manage projects they own
  - Can view/work on projects they are added to
  - Can update status of tasks assigned to them

=====================================================
PROJECT STRUCTURE
=====================================================

team_task_manager/
├── manage.py
├── requirements.txt
├── Procfile              <- Railway deployment
├── runtime.txt           <- Python version
├── .env.example          <- Environment variables template
├── README.txt            <- This file
├── team_task_manager/    <- Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/             <- User auth & roles
│   ├── models.py         <- Custom User model
│   ├── views.py          <- Login/Signup/Logout
│   ├── serializers.py    <- REST serializers
│   ├── api_views.py      <- REST API views
│   └── urls.py
├── projects/             <- Project management
│   ├── models.py
│   ├── views.py          <- Web UI views
│   ├── api_views.py      <- REST API views
│   └── urls.py
├── tasks/                <- Task management
│   ├── models.py
│   ├── views.py
│   ├── api_views.py
│   └── urls.py
├── templates/            <- HTML templates (Bootstrap 5)
│   ├── base.html
│   ├── dashboard.html
│   ├── accounts/
│   ├── projects/
│   └── tasks/
└── static/               <- CSS, JS files
