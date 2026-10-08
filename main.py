from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.8-flash")




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Or use ["*"] to allow all origins (not recommended for production)
    allow_credentials=False,        # Allow cookies and authorization headers
    allow_methods=["*"],           # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],           # Allow all headers
)
class Prompt(BaseModel):
    text: str

@app.get("/") # /: endpoint for home page 
def home():
    return {"message": "FastAPI is server running!"}
@app.post("/generate") 
def generate_response(prompt: Prompt):
    response = model.generate_content(prompt.text)
    return{
        "response": response.text

    }
    