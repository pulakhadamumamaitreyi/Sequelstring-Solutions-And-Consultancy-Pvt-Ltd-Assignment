from fastapi import FastAPI

app = FastAPI(
    title="AI Research & Knowledge Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Research & Knowledge Assistant is Running"
    }
