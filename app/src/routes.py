from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from src.im_service import InfectionMonkeyService
from src.conf import config

from os import listdir
from typing import List

class ApiResponse(BaseModel):
    code: int
    message: str

class ConfList(BaseModel):
    configs: List[str]

monkey = InfectionMonkeyService()
router = APIRouter()

@router.get("/run/{conf_name}", tags=["Run"], response_model=ApiResponse)
async def run_island(conf_name: str):
    monkey.run_island(conf_name)
    return JSONResponse(content={"code": 200, "message": "Monkey Island Running"})

@router.get("/configs", tags=["Config"], response_model=ConfList)
async def get_configs():
    return JSONResponse(content={"configs": [f for f in listdir(config.INFECTION_MONKEY_CONFIG)]})

@router.get("/kill", tags=["Run"], response_model=ApiResponse)
async def kill_monkeys():
    monkey.kill()
    return JSONResponse(content={"code": 200, "message": "KILL signaled to all Monkeys"})

@router.get("/reset", tags=["Run"], response_model=ApiResponse)
async def reset():
    monkey.reset()
    return JSONResponse(content={"code": 200, "message": "Monkey environment successfully reset"})