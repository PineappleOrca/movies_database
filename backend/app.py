from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import movies
import uvicorn

app = FastAPI(title="Movies Database API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:8000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers (this is where APIRouter gets registered)
app.include_router(movies.router)
#app.include_router(wishlist.router)
#app.include_router(stats.router)

@app.get("/")
def root():
    return {"message": "Movies Database API"}

if __name__ == "__main__":
    uvicorn.run("backend.api:app", host="0.0.0.0", port=8000, reload=True)