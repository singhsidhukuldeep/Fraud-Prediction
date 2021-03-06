# Fraud-Prediction
Fraud detection model for synthetic dataset of money transactions. 


## Setup

### Dependencies setup

```shell
pip install -r requirements.txt
```

### Running the Server

```shell
uvicorn main:app --host 127.0.0.1 --port 8000 --reload --workers 4
```

here:
`127.0.0.1` is the host location and
`8000` is the port


GUI(s):
 * `{HOST}}/docs` >> This yields the OpenAPI Swagger UI. Eg: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
 * `{HOST}}/redoc` >> This uses the Redoc UI with some documentations out of the box. Eg: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


### Deployed Endpoints [all using free hostings so be patient]

- Heroku: https://fraud-prediction.herokuapp.com/
    - [GET/POST] https://fraud-prediction.herokuapp.com/ping check if the service is up
    - [GET/POST] https://fraud-prediction.herokuapp.com/reset resets the database
    - [POST] https://fraud-prediction.herokuapp.com/is-fraud get prediction if the payment is fraud or not
    - OpenAPI Swagger UI: https://fraud-prediction.herokuapp.com/docs
    - Redoc UI with some documentations: https://fraud-prediction.herokuapp.com/redoc

- Deta: https://3dw8p7.deta.dev/ [down for time being, will redeploy soon]