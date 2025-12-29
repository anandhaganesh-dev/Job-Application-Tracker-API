# Job Application Tracker API

A backend REST API built with FastAPI that helps users track and manage their job applications securely.

## 🚀 Features
- User registration & login (JWT authentication)
- Create, update, delete job applications
- Job status tracking (Applied, Interview, Offer, Rejected)
- Ownership-based access control
- Filtering & pagination
- PostgreSQL database
- API versioning (/api/v1)

## 🛠 Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Pydantic

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd job-tracker-api
### 2. Create virtual environment in IDE
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables
cp .env.example .env

Update values inside .env.

### 5. Run the server
uvicorn app.main:app --reload

### 6. Open API docs
http://127.0.0.1:8000/docs

🔐 API Endpoints (Sample)

POST /api/v1/auth/register

POST /api/v1/auth/login

GET /api/v1/jobs

POST /api/v1/jobs

PUT /api/v1/jobs/{id}

DELETE /api/v1/jobs/{id}

📌 Future Improvements

Frontend integration (React)

Email reminders

AI resume analyzer integration

Docker deployment