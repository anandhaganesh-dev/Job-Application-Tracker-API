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
- Testing using pytest

## 🛠 Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Pydantic
- Pytest

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/anandhaganesh-dev/Job-Application-Tracker-API.git
cd Job-Application-Tracker-API
### 2. Create virtual environment in IDE
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### Optional 
pytest # test the routes 

### 4. Configure environment variables
cp .env.example .env

Update values inside .env

### 5. Run the server
uvicorn app.main:app --reload

### 6. Open API docs
http://127.0.0.1:8000/docs

🔐 API Endpoints (Sample)

POST /api/v1/auth/register

POST /api/v1/auth/login

GET /api/v1/jobs

GET /api/v1/jobs/{id}

POST /api/v1/jobs

PUT /api/v1/jobs/{id}

DELETE /api/v1/jobs/{id}

📌 Future Improvements

Frontend integration (React)

ADD Role based access , refresh tokens