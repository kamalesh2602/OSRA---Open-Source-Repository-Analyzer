from fastapi import FastAPI

app = FastAPI(
    title="OSRA API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "OSRA API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }