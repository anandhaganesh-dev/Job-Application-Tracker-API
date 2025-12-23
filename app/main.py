from fastapi import FastAPI

app = FastAPI(title="Job-Applications-Tracker-API")

@app.get("/")
def root():
    return {"message": "Job Application Tracker API is running"}