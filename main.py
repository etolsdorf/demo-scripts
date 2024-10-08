from fastapi import FastAPI

app = FastAPI(
        title="AI-MD",
        description="AI-MD",
       )

@app.get("/")
def read_root():
    return {"result": "Hello, DOKTOR CONNECT!"}