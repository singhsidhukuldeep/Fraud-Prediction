import requests

r = requests.post('http://127.0.0.1:8000/ping')
print('POST ping',r.status_code, r.json())

r = requests.get('http://127.0.0.1:8000/ping')
print('GET ping',r.status_code, r.json())

r = requests.post('http://127.0.0.1:8000/reset')
print('POST reset',r.status_code, r.json())

r = requests.get('http://127.0.0.1:8000/reset')
print('GET reset',r.status_code, r.json())

r = requests.post('http://127.0.0.1:8000/is-fraud', json = {
"step":1,
"type":"PAYMENT",
"amount":9839.64,
"nameOrig":"C1231006815",
"oldbalanceOrig":170136.0,
"newbalanceOrig":160296.36,
"nameDest":"M1979787155",
"oldbalanceDest":0.0,
"newbalanceDest":0.0
})
print('POST is-fraud',r.status_code, r.json())

r = requests.post('http://127.0.0.1:8000/is-fraud', json = {
"step":1,
"type":"PAYMENT",
"amount":9839.64,
"nameOrig":"C1231006815",
"oldbalanceOrig":170136.0,
"newbalanceOrig":160296.36,
"nameDest":"M1979787155",
"oldbalanceDest":0.0,
"newbalanceDest":0.0
})
print('POST is-fraud',r.status_code, r.json())

r = requests.post('http://127.0.0.1:8000/is-fraud', json = {
"step":2,
"type":"PAYMENTT",
"amount":9839.64,
"nameOrig":"C1231006815",
"oldbalanceOrig":170136.0,
"newbalanceOrig":160296.36,
"nameDest":"M1979787155",
"oldbalanceDest":0.0,
"newbalanceDest":0.0
})
print('POST is-fraud',r.status_code, r.json())