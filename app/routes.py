from fastapi import APIRouter

router = APIRouter()

@router.get("/advice/start")
def initial_advice():
    return {"advice": "This is your initial riding advice"}
