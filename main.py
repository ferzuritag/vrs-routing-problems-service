from fastapi import FastAPI
from routes.routing_problems import routing_problems
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(routing_problems)