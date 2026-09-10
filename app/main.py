from fastapi import FastAPI


app = FastAPI(title="AI-Playground-API")

@app.get('/')
def root():
    return {"message: AI Plaground API is running...."}