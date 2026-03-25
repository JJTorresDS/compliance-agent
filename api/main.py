from fastapi import FastAPI
from graph.pipeline import run_pipeline


app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/analyze/{alert_id}")
def analyze(alert_id: str):
    return run_pipeline(alert_id)