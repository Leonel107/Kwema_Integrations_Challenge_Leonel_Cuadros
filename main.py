from fastapi import FastAPI
from models.programmer_profile import Programmer_Profiles
from routers.profile import router as profile_router

kwema = FastAPI()

@kwema.get('/')
def message():
    return "kwema-integrations-challenge"

kwema.include_router(profile_router)



