from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Resume Builder API")

# Configure CORS so the frontend HTML can communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model incoming resume data ko validate karne ke liye
class ResumeData(BaseModel):
    name: str
    email: str
    education: str
    experience_title: Optional[str] = None
    experience_desc: Optional[str] = None
    skills: str
    template: str

@app.post("/api/resume")
async def create_resume(resume: ResumeData):
    # Yeh backend ka endpoint hai jo frontend se data receive karega
    processed_data = {
        "status": "success",
        "message": "Resume data received and validated successfully.",
        "data": resume.dict()
    }
    return processed_data

@app.get("/")
async def health_check():
    return {"status": "Backend is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)