from fastapi import FastAPI

app = FastAPI(
        title="AI-MD",
        description="AI-MD",
        docs_url="/",
        swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
        openapi_url="/openapi.json",)

@app.get("/")
def read_root():
    return {"result": "Hello, DOKTOR CONNECT!"}