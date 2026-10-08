from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.8-flash")

class Prompt(BaseModel):
    text: str


app = FastAPI()

@app.get("/") # /: endpoint for home page 
def home():
    return {"message": "FastAPI is server running!"}
@app.post("/generate") 
def generate_response(prompt: Prompt):
    response = model.generate_content(prompt.text)
    return{
        "response": response.text
        
    }
    