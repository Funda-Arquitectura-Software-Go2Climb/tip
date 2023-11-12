from fastapi import FastAPI
from routes.tip_routes import tip_router
app = FastAPI()

app.include_router(tip_router)