from fastapi import FastAPI
from routes.index import user, auth_login

app = FastAPI()

app.include_router(user)
app.include_router(auth_login)