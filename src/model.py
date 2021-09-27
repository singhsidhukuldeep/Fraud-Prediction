import pickle
from xgboost.sklearn import XGBClassifier
import xgboost
import pandas as pd

model = XGBClassifier()
model_location = "./src/xgb_v1.bin"
model.load_model(model_location)


def transform(inp, step_amnt_nDst_cnt):
    def _transform(
        step,
        type,
        amount,
        nameOrig,
        oldbalanceOrig,
        newbalanceOrig,
        nameDest,
        oldbalanceDest,
        newbalanceDest,
    ):
        return [
            {
                "step": step,
                "amount": amount,
                "oldbalanceOrig": oldbalanceOrig,
                "newbalanceOrig": newbalanceOrig,
                "oldbalanceDest": oldbalanceDest,
                "newbalanceDest": newbalanceDest,
                "debit": oldbalanceOrig - newbalanceOrig,
                "credit": newbalanceDest - oldbalanceDest,
                "bal0Orig": oldbalanceOrig == newbalanceOrig == 0,
                "bal0Dest": oldbalanceDest == newbalanceDest == 0,
                "credit_error": newbalanceDest - oldbalanceDest - amount,
                "debit_error": oldbalanceOrig - newbalanceOrig - amount,
                "step_amnt_nDst_cnt": 1,  # ['step','amount','nameDest'] count
                "type_encoded": 1
                if type == "CASH_OUT"
                else 0,  # only ['CASH_OUT', 'TRANSFER']
            }
        ]

    ret = _transform(
        step=inp.step,
        type=inp.type,
        amount=inp.amount,
        nameOrig=inp.nameOrig,
        oldbalanceOrig=inp.oldbalanceOrig,
        newbalanceOrig=inp.newbalanceOrig,
        nameDest=inp.nameDest,
        oldbalanceDest=inp.oldbalanceDest,
        newbalanceDest=inp.newbalanceDest,
    )
    ret[0]["step_amnt_nDst_cnt"] = step_amnt_nDst_cnt
    return pd.DataFrame(ret)


def predict_on_model(model, inp):
    return model.predict(inp)
