from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from views import social_router, account_router, search_router

app = FastAPI()
router = APIRouter()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(social_router)
app.include_router(account_router)
app.include_router(search_router)
