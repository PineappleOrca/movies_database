from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"}

uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)