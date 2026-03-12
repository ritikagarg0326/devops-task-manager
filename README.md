🚀 DevOps Task Manager

A containerized, production-ready microservices application that demonstrates secure authentication, user-scoped dashboards, and dynamic profile management using JWT and Docker.

📌 Overview

DevOps Task Manager is a multi-user web application built with:

🐍 Flask (Authentication Service)

🌐 Nginx (Reverse Proxy + Static Frontend)

🍃 MongoDB (Persistent Database)

🐳 Docker & Docker Compose (Container Orchestration)

The application allows users to:

Register securely

Login using JWT authentication

Access a personalized dashboard

Add and manage skills dynamically

Maintain persistent data across container restarts

🏗 Architecture
Browser
   ↓
Nginx (Frontend + Reverse Proxy)
   ↓
Flask Auth Service (JWT + Business Logic)
   ↓
MongoDB (Persistent Storage via Docker Volume)
🔹 Microservices Design

Frontend served by Nginx

Authentication handled by Flask service

Data persisted in MongoDB

Services communicate via Docker internal network

🔐 Features

✔ Multi-user support
✔ JWT-based stateless authentication
✔ User-specific dashboard
✔ Dynamic skill management
✔ Persistent MongoDB storage
✔ Reverse proxy configuration
✔ Dockerized microservices
✔ Production-style separation of concerns

<img width="928" height="586" alt="Screenshot 2026-02-25 192018" src="https://github.com/user-attachments/assets/e4e08c38-f974-4820-9c4e-5a87d694edbd" />

<img width="977" height="587" alt="Screenshot 2026-02-25 192118" src="https://github.com/user-attachments/assets/14a64bde-3954-4f86-a07a-c3ef5aba76c1" />

🧠 Authentication Flow

User registers with username & password

Password is securely hashed using bcrypt

On login:

JWT token is generated

Token stored in browser

Token is used for:

Accessing protected routes

Fetching user-specific data

Adding skills

📂 Project Structure
devops-task-manager/
│
├── docker-compose.yml
├── .env
│
├── frontend/
│   ├── index.html
│   ├── home.html
│   └── style.css
│
├── nginx/
│   └── default.conf
│
└── auth-service/
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
🐳 Running the Application
1️⃣ Clone the repository
git clone <repo-url>
cd devops-task-manager
2️⃣ Start containers
docker compose up --build
3️⃣ Access application
http://localhost
🗄 Data Persistence

MongoDB uses a named Docker volume:

mongo_data

Data remains intact even after:

docker compose down

To reset database:

docker compose down -v
🔍 API Endpoints
Method	Endpoint	Description
POST	/register	Register user
POST	/login	Login & receive JWT
GET	/profile	Get user profile (protected)
POST	/add-skill	Add skill (protected)
GET	/health	Health check
🔐 Security Practices

Password hashing using bcrypt

Stateless JWT authentication

Protected API endpoints

User-scoped database queries

Service isolation via Docker network

🚀 Production-Ready Design Principles

Separation of frontend and backend services

Reverse proxy pattern

Containerized deployment

Environment-based configuration

Persistent storage

Health check endpoint

🎯 Future Improvements

Role-based access control (RBAC)

Kubernetes deployment (EKS-ready)

CI/CD pipeline integration

Rate limiting

Token refresh mechanism

Skill edit/delete functionality in website

Monitoring stack (Prometheus + Grafana)
