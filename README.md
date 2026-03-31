# Feedback Application (Dockerized)

This is a full-stack Feedback Application with:

* FastAPI (Backend)
* React + Vite (Frontend)
* PostgreSQL (Database)

The entire project is containerized using Docker.

---

## 🚀 Prerequisites

Install Docker:

* Windows / Mac: Docker Desktop
* Linux: Docker Engine

---

## 📥 Setup

Clone the repository:

```bash
git clone <your-repo-url>
cd DevOps_X
```

Create environment files:

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

---

## ▶️ Run the Application

```bash
docker-compose up --build
```

---

## 🌐 Access the App

Frontend:

```
http://localhost
```

Backend API:

```
http://localhost:8000
```

---

## ⏹️ Stop the Application

```bash
docker-compose down
```

---

## 🧹 Reset Everything (Optional)

```bash
docker-compose down -v
```

---

## 🔄 Restart Backend (if needed)

```bash
docker-compose restart backend
```

---

## 📌 Notes

* If you see database errors on first run, restart backend:

  ```bash
  docker-compose restart backend
  ```
* This happens because the database may take a few seconds to initialize.

---

## 🐳 Tech Stack

* FastAPI
* React (Vite)
* PostgreSQL
* Docker & Docker Compose

---

## ✅ One Command Run

After setup, the entire application runs using:

```bash
docker-compose up --build
```

---

## 👨‍💻 Author

Mayank Roy
