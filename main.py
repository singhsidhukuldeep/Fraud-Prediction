from fastapi import FastAPI, Body, Depends
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from os import remove

import src.ping
import src.is_fraud
import src.db_process

reset_db = lambda: remove("all_requests.db")


class payment_fraud_check_input(BaseModel):
    step: int
    type: str
    amount: float
    nameOrig: str
    oldbalanceOrig: float
    newbalanceOrig: float
    nameDest: str
    oldbalanceDest: float
    newbalanceDest: float

    class Config:
        orm_mode = True


app = FastAPI()


@app.get("/ping")
async def ping_get(db: Session = Depends(src.db_process.get_db)):
    cnt = db.query(func.count(src.db_process.apiCalls.id)).scalar()
    ret = src.ping.response_ping()
    ret["db_count"] = cnt
    return ret


@app.post("/ping")
async def ping_post(db: Session = Depends(src.db_process.get_db)):
    cnt = db.query(func.count(src.db_process.apiCalls.id)).scalar()
    ret = src.ping.response_ping()
    ret["db_count"] = cnt
    return ret


@app.get("/reset")
async def reset_get():
    try:
        reset_db()
        src.db_process.Base.metadata.create_all(bind=src.db_process.engine)
        return {"status": "RESET DONE"}
    except Exception as exp:
        return {"status": f"{exp}"}


@app.post("/reset")
async def reset_post():
    try:
        reset_db()
        src.db_process.Base.metadata.create_all(bind=src.db_process.engine)
        return {"status": "RESET DONE"}
    except Exception as exp:
        return {"status": f"{exp}"}


@app.post("/is-fraud")
async def is_fraud_post(
    inp: payment_fraud_check_input, db: Session = Depends(src.db_process.get_db)
):
    curr_call = src.db_process.apiCalls()
    curr_call.step = inp.step
    curr_call.type = inp.type
    curr_call.amount = inp.amount
    curr_call.nameOrig = inp.nameOrig
    curr_call.oldbalanceOrig = inp.oldbalanceOrig
    curr_call.newbalanceOrig = inp.newbalanceOrig
    curr_call.nameDest = inp.nameDest
    curr_call.oldbalanceDest = inp.oldbalanceDest
    curr_call.newbalanceDest = inp.newbalanceDest
    db.add(curr_call)
    db.commit()
    step_amnt_nDst_cnt = (
        db.query(func.count(src.db_process.apiCalls.id))
        .filter(src.db_process.apiCalls.step == inp.step)
        .filter(src.db_process.apiCalls.amount == inp.amount)
        .filter(src.db_process.apiCalls.nameDest == inp.nameDest)
        .scalar()
    )
    return src.is_fraud.response_is_fraud(inp, step_amnt_nDst_cnt)
