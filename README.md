<a id="readme-top"></a>

<!-- BADGES -->

[![GitHub Stars](https://img.shields.io/github/stars/iprashanthvanam/team-task-manager?style=for-the-badge&color=f59e0b)](https://github.com/iprashanthvanam/team-task-manager/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/iprashanthvanam/team-task-manager?style=for-the-badge&color=3b82f6)](https://github.com/iprashanthvanam/team-task-manager/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/iprashanthvanam/team-task-manager?style=for-the-badge&color=ef4444)](https://github.com/iprashanthvanam/team-task-manager/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.15-red?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Railway-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://railway.app)
[![Deployed on Railway](https://img.shields.io/badge/Deployed%20on-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app)

---

<div align="center">

# ✅ Team Task Manager

### Full-Stack Django Project & Task Management Web App

_A role-based team collaboration tool to create projects, assign tasks, and track progress — with a full REST API and live Railway deployment._

<br/>

[🚀 Live Demo](https://team-task-manager-webapp.up.railway.app/) · [🐛 Report Bug](https://github.com/iprashanthvanam/team-task-manager/issues/new?labels=bug) · [✨ Request Feature](https://github.com/iprashanthvanam/team-task-manager/issues/new?labels=enhancement)

</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>📑 Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#system-architecture">System Architecture</a></li>
    <li><a href="#roles-explained">Roles Explained</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#environment-variables">Environment Variables</a></li>
    <li><a href="#api-reference">API Reference</a></li>
    <li><a href="#deployment">Deployment — Railway</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

Modern teams juggle multiple projects, shifting priorities, and distributed members — yet most task tools are either too complex or lack proper access control for small teams.

**Team Task Manager** solves this with a clean, lightweight web application where Admins can oversee all work across the organisation and Members can manage their own projects and tasks — all with a full REST API for integration with any frontend or external tool.

**Why Team Task Manager?**

- ❌ **Old approach:** Spreadsheets and chat threads with no structure, no access control, and no overdue tracking
- ✅ **Our approach:** Role-based project and task management with a live dashboard, REST API, JWT auth, and one-click Railway deployment backed by PostgreSQL

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Screenshots

A complete visual walkthrough of the application.

---

### 🔐 Login Page

<div align="center">
  <img src="screenshots/login.png" alt="Team Task Manager — Login Page" width="860"/>
  <br/><br/>
  <sub><b>Secure login with session authentication.</b> Redirects to the dashboard on success, with proper error messages for invalid credentials.</sub>
</div>

---

### 📝 Sign Up Page

<div align="center">
  <img src="screenshots/signup.png" alt="Team Task Manager — Sign Up Page" width="860"/>
  <br/><br/>
  <sub><b>Account creation with role selection.</b> Users can sign up as Admin or Member. Duplicate username and email validation is enforced server-side.</sub>
</div>

---

### 📊 Dashboard

<div align="center">
  <img src="screenshots/dashboard.png" alt="Team Task Manager — Dashboard" width="860"/>
  <br/><br/>
  <sub><b>Central command view.</b> Displays total projects, task counts by status (Todo / In Progress / Done), overdue tasks, recent activity, and tasks assigned to the current user.</sub>
</div>

---

### 📁 Projects List

<div align="center">
  <img src="screenshots/projects.png" alt="Team Task Manager — Projects List" width="860"/>
  <br/><br/>
  <sub><b>All accessible projects in one view.</b> Admins see every project; Members see only their owned or assigned projects.</sub>
</div>

---

### 📋 Task Management

<div align="center">
  <img src="screenshots/tasks.png" alt="Team Task Manager — Task Management" width="860"/>
  <br/><br/>
  <sub><b>Full task management with filters.</b> Filter by status, priority, project, or view only your assigned tasks. Overdue tasks are highlighted automatically.</sub>
</div>

---

## Key Features

### 🔐 Authentication & Access Control

- **Signup & Login** — session-based authentication for the web UI, JWT for the REST API
- **Role-based access control** — Admin and Member roles with separate permission levels enforced on every view and API endpoint
- **Profile management** — users can view their account details

### 📁 Project Management

- **Create, edit, delete projects** — with name, description, and member assignment
- **Team membership** — project owners can add/remove members; Admins manage all projects
- **Access enforcement** — members can only see and interact with projects they own or belong to

### ✅ Task Management

- **Full CRUD** — create, view, edit, and delete tasks within any accessible project
- **Status tracking** — Todo → In Progress → Done with quick status update support
- **Priority levels** — Low, Medium, High with colour-coded badges
- **Assignment** — assign tasks to any project member
- **Due dates & overdue detection** — tasks past their due date are automatically flagged
- **Task filters** — filter by status, priority, project, or assigned-to-me

### 📊 Dashboard

- Total projects and tasks at a glance
- Task counts by status (Todo, In Progress, Done)
- Overdue task count
- Recent tasks and my assigned tasks panels

### 🔌 REST API

- Full JWT authentication via `/api/token/`
- CRUD endpoints for users, projects, and tasks
- Overdue tasks and my-tasks custom actions
- Pagination and filtering via query parameters
- Django Admin panel at `/admin/`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Tech Stack

| Layer            | Technology                                                   |
| ---------------- | ------------------------------------------------------------ |
| **Backend**      | Django 4.2, Django REST Framework 3.15                       |
| **Database**     | PostgreSQL (Railway production) / SQLite (local development) |
| **Auth**         | Session-based (Web UI) + JWT via SimpleJWT (REST API)        |
| **Frontend**     | Django Templates, Bootstrap 5                                |
| **Static Files** | WhiteNoise (compressed, manifest-based)                      |
| **Deployment**   | Railway (Gunicorn + PostgreSQL plugin)                       |
| **Config**       | python-decouple, dj-database-url                             |
| **CORS**         | django-cors-headers                                          |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    BROWSER (Bootstrap 5 UI)                  │
│         Login · Signup · Dashboard · Projects · Tasks        │
└─────────────────────────┬────────────────────────────────────┘
                          │ HTTP (session cookie / JWT)
┌─────────────────────────▼────────────────────────────────────┐
│                    DJANGO APPLICATION                        │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  accounts/   │  │  projects/   │  │     tasks/       │   │
│  │  views.py    │  │  views.py    │  │    views.py      │   │
│  │  api_views   │  │  api_views   │  │    api_views     │   │
│  └──────────────┘  └──────────────┘  └──────────────────┘   │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐   │
│  │               Django REST Framework                   │   │
│  │    JWT Auth · Serializers · ViewSets · Pagination     │   │
│  └───────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐   │
│  │                   Django ORM                          │   │
│  │     User ──< Task >── Project ──< ProjectMember       │   │
│  └───────────────────────┬───────────────────────────────┘   │
└────────────────────────── │ ─────────────────────────────────┘
                            │
              ┌─────────────▼──────────────┐
              │  PostgreSQL (Railway)       │
              │  SQLite (local dev)         │
              └────────────────────────────┘
```

---

## Roles Explained

| Capability                    | Admin | Member                        |
| ----------------------------- | ----- | ----------------------------- |
| View all projects             | ✅    | ❌ (own/assigned only)        |
| Create projects               | ✅    | ✅                            |
| Edit / delete any project     | ✅    | ❌ (own only)                 |
| View all tasks                | ✅    | ❌ (accessible projects only) |
| Create tasks                  | ✅    | ✅                            |
| Edit / delete any task        | ✅    | ❌ (own/created only)         |
| Update task status (assigned) | ✅    | ✅                            |
| Access Django `/admin/` panel | ✅    | ❌                            |
| Manage all users via API      | ✅    | ❌ (self only)                |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Prerequisites

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y
```

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/iprashanthvanam/team-task-manager.git
cd team-task-manager
```

**2. Create and activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

```bash
cp .env.example .env
nano .env   # Set your SECRET_KEY
```

**5. Run migrations**

```bash
python manage.py migrate
```

**6. Create a superuser (Admin account)**

```bash
python manage.py createsuperuser
# Enter username, email, and password when prompted
```

**7. Collect static files** _(optional for local dev)_

```bash
python manage.py collectstatic --no-input
```

**8. Start the development server**

```bash
python manage.py runserver
```

**9. Open in your browser**

```
http://localhost:8000/
```

> **One-click setup:** Alternatively, run `chmod +x setup.sh && ./setup.sh` — it handles steps 2–7 automatically.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

| Variable        | Description                               | Example                |
| --------------- | ----------------------------------------- | ---------------------- |
| `SECRET_KEY`    | Django secret key — keep this private     | `django-insecure-...`  |
| `DEBUG`         | Set to `False` in production              | `True`                 |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames | `localhost,127.0.0.1`  |
| `DATABASE_URL`  | Database connection string                | `sqlite:///db.sqlite3` |

**Generate a secure SECRET_KEY:**

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**On Railway**, `DATABASE_URL` is automatically injected by the PostgreSQL plugin — you do not need to set it manually.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## API Reference

All API endpoints are prefixed with `/api/`. JWT authentication is required except for `/api/register/` and `/api/token/`.

### Authentication

| Method | Endpoint              | Description                        |
| ------ | --------------------- | ---------------------------------- |
| `POST` | `/api/token/`         | Obtain JWT access + refresh tokens |
| `POST` | `/api/token/refresh/` | Refresh an expired access token    |
| `POST` | `/api/register/`      | Register a new user account        |

### Users

| Method          | Endpoint           | Description                                |
| --------------- | ------------------ | ------------------------------------------ |
| `GET`           | `/api/users/`      | List users (Admin: all; Member: self only) |
| `GET`           | `/api/users/me/`   | Current authenticated user info            |
| `GET/PUT/PATCH` | `/api/users/{id}/` | Retrieve or update a user                  |

### Projects

| Method      | Endpoint                         | Description               |
| ----------- | -------------------------------- | ------------------------- |
| `GET`       | `/api/projects/`                 | List accessible projects  |
| `POST`      | `/api/projects/`                 | Create a new project      |
| `GET`       | `/api/projects/{id}/`            | Retrieve a project        |
| `PUT/PATCH` | `/api/projects/{id}/`            | Update a project          |
| `DELETE`    | `/api/projects/{id}/`            | Delete a project          |
| `POST`      | `/api/projects/{id}/add_member/` | Add a member to a project |

### Tasks

| Method      | Endpoint               | Description                                                            |
| ----------- | ---------------------- | ---------------------------------------------------------------------- |
| `GET`       | `/api/tasks/`          | List accessible tasks (supports `?status=`, `?priority=`, `?project=`) |
| `POST`      | `/api/tasks/`          | Create a new task                                                      |
| `GET`       | `/api/tasks/{id}/`     | Retrieve a task                                                        |
| `PUT/PATCH` | `/api/tasks/{id}/`     | Update a task                                                          |
| `DELETE`    | `/api/tasks/{id}/`     | Delete a task                                                          |
| `GET`       | `/api/tasks/overdue/`  | List all overdue tasks                                                 |
| `GET`       | `/api/tasks/my_tasks/` | List tasks assigned to the current user                                |

### Example — Get JWT token

```bash
curl -X POST https://your-app.railway.app/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

Response:

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Example — Create a project

```bash
curl -X POST https://your-app.railway.app/api/projects/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "Website Redesign", "description": "Q3 redesign project"}'
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Deployment — Railway

This app is production-ready for Railway with PostgreSQL. The `Procfile` handles everything automatically on deploy.

### Step-by-step

**1. Push your code to GitHub**

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/iprashanthvanam/team-task-manager.git
git push -u origin main
```

**2. Create a Railway project**

- Go to [railway.app](https://railway.app) and create an account
- Click **New Project → Deploy from GitHub repo**
- Select your `team-task-manager` repository

**3. Add PostgreSQL**

- Inside your Railway project, click **+ New → Database → Add PostgreSQL**
- Railway automatically sets the `DATABASE_URL` environment variable

**4. Set environment variables** in Railway dashboard → Variables:

| Variable        | Value                                     |
| --------------- | ----------------------------------------- |
| `SECRET_KEY`    | _(generate a strong key — see above)_     |
| `DEBUG`         | `False`                                   |
| `ALLOWED_HOSTS` | `your-app.railway.app`                    |
| `DATABASE_URL`  | _(auto-set by Railway PostgreSQL plugin)_ |

**5. Railway auto-runs your Procfile on every deploy:**

```
release: python manage.py migrate --no-input && python manage.py collectstatic --no-input
web: gunicorn team_task_manager.wsgi --log-file -
```

**6. Create your superuser via Railway console:**

```bash
python manage.py createsuperuser
```

Your app will be live at `https://your-app.railway.app` 🎉

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project Structure

```
team_task_manager/
├── manage.py
├── requirements.txt
├── Procfile                      ← Railway deployment config
├── runtime.txt                   ← Python version pin (3.11.7)
├── setup.sh                      ← One-click local setup script
├── .env.example                  ← Environment variables template
├── README.md                     ← This file
│
├── team_task_manager/            ← Django project config
│   ├── settings.py               ← All settings (decouple + dj-database-url)
│   ├── urls.py                   ← Root URL routing
│   └── wsgi.py
│
├── accounts/                     ← User auth & role management
│   ├── models.py                 ← Custom User model (AbstractUser + role)
│   ├── views.py                  ← Signup / Login / Logout / Profile
│   ├── serializers.py            ← REST serializers
│   ├── api_views.py              ← REST API ViewSets
│   ├── api_urls.py               ← API URL routing
│   ├── urls.py                   ← Web UI URL routing
│   └── migrations/
│
├── projects/                     ← Project management
│   ├── models.py                 ← Project model (owner FK + members M2M)
│   ├── views.py                  ← Web UI views (CRUD + dashboard)
│   ├── api_views.py              ← REST API ViewSet + add_member action
│   ├── serializers.py
│   ├── urls.py                   ← Web UI URL routing
│   ├── api_urls.py               ← API URL routing
│   ├── dashboard_urls.py         ← Dashboard URL routing
│   └── migrations/
│
├── tasks/                        ← Task management
│   ├── models.py                 ← Task model (status, priority, due_date)
│   ├── views.py                  ← Web UI views (CRUD + filters + status toggle)
│   ├── api_views.py              ← REST API ViewSet + overdue + my_tasks actions
│   ├── serializers.py
│   ├── urls.py                   ← Web UI URL routing
│   ├── api_urls.py               ← API URL routing
│   └── migrations/
│
├── templates/                    ← HTML templates (Bootstrap 5)
│   ├── base.html                 ← Base layout with navbar
│   ├── dashboard.html            ← Main dashboard
│   ├── accounts/
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── profile.html
│   ├── projects/
│   │   ├── list.html
│   │   ├── detail.html
│   │   ├── create.html
│   │   ├── edit.html
│   │   └── confirm_delete.html
│   └── tasks/
│       ├── list.html
│       ├── detail.html
│       ├── create.html
│       ├── edit.html
│       └── confirm_delete.html
│
└── static/
    ├── css/style.css
    └── js/main.js
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

- [x] Custom User model with Admin / Member roles
- [x] Session-based authentication (web UI)
- [x] JWT authentication (REST API)
- [x] Project CRUD with owner and member management
- [x] Task CRUD with status, priority, due date, and assignment
- [x] Overdue task detection and dashboard stats
- [x] Full REST API with DRF ViewSets
- [x] Railway deployment with PostgreSQL
- [x] WhiteNoise static file serving
- [ ] Email notifications on task assignment or overdue
- [ ] Task comments and activity log
- [ ] Kanban board view (drag-and-drop status columns)
- [ ] File attachments on tasks
- [ ] Admin analytics — project completion rates and team velocity
- [ ] Docker Compose for one-command local setup
- [ ] Slack / webhook integration for task updates

See the [open issues](https://github.com/iprashanthvanam/team-task-manager/issues) for the full list of proposed features and known bugs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Contributions are what make open-source great. Any contributions are **greatly appreciated**.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure your code follows the existing structure and includes appropriate validation. For significant changes, open an issue first to discuss the approach.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

<div align="center">

### Prashanth Vanam

<p>
  <a href="mailto:prashanthvanamnetha@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-prashanthvanamnetha%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://www.linkedin.com/in/iprashanthvanam/">
    <img src="https://img.shields.io/badge/LinkedIn-iprashanthvanam-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://github.com/iprashanthvanam">
    <img src="https://img.shields.io/badge/GitHub-iprashanthvanam-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/📍%20Location-Hyderabad%2C%20India-f59e0b?style=for-the-badge"/>
  &nbsp;
  <img src="https://img.shields.io/badge/📞%20Mobile-%2B91%2070361%2042499-25D366?style=for-the-badge"/>
</p>

</div>

<br/>

|                 |                                                                                 |
| --------------- | ------------------------------------------------------------------------------- |
| 📧 **Email**    | [prashanthvanamnetha@gmail.com](mailto:prashanthvanamnetha@gmail.com)           |
| 💼 **LinkedIn** | [linkedin.com/in/iprashanthvanam](https://www.linkedin.com/in/iprashanthvanam/) |
| 🐙 **GitHub**   | [github.com/iprashanthvanam](https://github.com/iprashanthvanam)                |
| 📍 **Location** | Hyderabad, Telangana, India                                                     |
| 📞 **Mobile**   | +91 703 6142 499                                                                |

<br/>

> 💬 Feel free to reach out for collaborations, questions, or just to say hi!

**Project Link:** [https://github.com/iprashanthvanam/team-task-manager](https://github.com/iprashanthvanam/team-task-manager)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Acknowledgments

- [Django](https://www.djangoproject.com/) — the web framework that made this possible
- [Django REST Framework](https://www.django-rest-framework.org/) — powerful and flexible REST API toolkit
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/) — JWT authentication for DRF
- [Bootstrap 5](https://getbootstrap.com/) — responsive frontend UI components
- [WhiteNoise](https://whitenoise.readthedocs.io/) — static file serving for Django in production
- [Railway](https://railway.app/) — simple, fast cloud deployment with PostgreSQL
- [dj-database-url](https://github.com/jazzband/dj-database-url) — database URL parsing for Django
- [python-decouple](https://github.com/HBNetwork/python-decouple) — environment variable management
- [TKREC](https://tkrec.ac.in/) — TKR College of Engineering and Technology

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<div align="center">

Built with ❤️ for TKREC · Next Gen Employability Program

⭐ Star this repo if Team Task Manager helped you!

</div>
