from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

generator = pipeline("text-generation", model="gpt2")

@app.get("/generate")
def generate(prompt: str):
    result = generator(prompt, max_length=50)
    return {"response": result[0]["generated_text"]}
