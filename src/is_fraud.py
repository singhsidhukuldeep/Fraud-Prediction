import pandas as pd
from .model import model, transform, predict_on_model


def response_is_fraud(inp, step_amnt_nDst_cnt):
    if inp.type not in ['CASH_OUT', 'TRANSFER']:
        return {"isFraud": False}
    inp = transform(inp, step_amnt_nDst_cnt)
    pred = predict_on_model(model, inp)
    return {"isFraud": bool(pred)}
